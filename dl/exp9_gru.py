"""
EXP 9: GRU (Gated Recurrent Unit)
- Faster training than LSTM
- Compares GRU vs LSTM vs SimpleRNN
- Analyses efficiency and accuracy trade-offs
- Evaluates suitability for real-time applications
"""

import numpy as np
import time
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, LSTM, SimpleRNN, Dense, Embedding, Dropout
import matplotlib.pyplot as plt

# ── Text Data ─────────────────────────────────────────────────────────────────
TEXT = """
Deep learning is a subset of machine learning which uses neural networks.
Neural networks are inspired by the structure of the human brain and neurons.
Recurrent neural networks are designed to work with sequential data inputs.
Gated recurrent units are a simplified version of long short term memory.
Long short term memory networks solve the vanishing gradient problem well.
Simple recurrent networks struggle to learn long range dependencies easily.
Training deep neural networks requires large datasets and computing power.
Gradient descent is the optimization algorithm used for learning weights.
Backpropagation through time is used to train recurrent neural networks now.
The gating mechanism in GRU uses reset and update gates for information flow.
LSTM uses three gates namely input forget and output for memory management.
GRU achieves comparable performance to LSTM with fewer parameters overall.
Real time applications benefit from GRU due to its faster inference speed.
""" * 6

TEXT = TEXT.strip()
chars    = sorted(set(TEXT))
n_chars  = len(chars)
char2idx = {c: i for i, c in enumerate(chars)}
idx2char = {i: c for c, i in char2idx.items()}

print(f"Text length : {len(TEXT)}")
print(f"Vocab size  : {n_chars}")

SEQ_LEN = 30
EPOCHS  = 20
UNITS   = 64

# ── Prepare data ──────────────────────────────────────────────────────────────
encoded = np.array([char2idx[c] for c in TEXT])
X, y   = [], []
for i in range(len(encoded) - SEQ_LEN):
    X.append(encoded[i: i + SEQ_LEN])
    y.append(encoded[i + SEQ_LEN])
X    = np.array(X)
y_oh = tf.keras.utils.to_categorical(y, num_classes=n_chars)
print(f"Samples     : {X.shape}")

# ── Model builders ────────────────────────────────────────────────────────────
def build_simple_rnn():
    m = Sequential([
        Embedding(n_chars, 16, input_length=SEQ_LEN),
        SimpleRNN(UNITS),
        Dense(n_chars, activation='softmax'),
    ])
    m.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return m

def build_lstm():
    m = Sequential([
        Embedding(n_chars, 16, input_length=SEQ_LEN),
        LSTM(UNITS, dropout=0.2),
        Dense(n_chars, activation='softmax'),
    ])
    m.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return m

def build_gru():
    m = Sequential([
        Embedding(n_chars, 16, input_length=SEQ_LEN),
        GRU(UNITS, dropout=0.2),
        Dense(n_chars, activation='softmax'),
    ])
    m.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return m

# ── Count parameters ──────────────────────────────────────────────────────────
rnn_params  = build_simple_rnn().count_params()
lstm_params = build_lstm().count_params()
gru_params  = build_gru().count_params()
print(f"\nModel Parameters:")
print(f"  SimpleRNN : {rnn_params:,}")
print(f"  LSTM      : {lstm_params:,}")
print(f"  GRU       : {gru_params:,}")

# ── Train & Time ──────────────────────────────────────────────────────────────
results = {}

for name, build_fn in [("SimpleRNN", build_simple_rnn),
                        ("LSTM",      build_lstm),
                        ("GRU",       build_gru)]:
    print(f"\nTraining {name} ...")
    model = build_fn()
    t0    = time.time()
    hist  = model.fit(X, y_oh, epochs=EPOCHS, batch_size=128,
                      validation_split=0.1, verbose=1)
    elapsed = time.time() - t0
    _, train_acc = model.evaluate(X, y_oh, verbose=0)

    results[name] = {
        'history':   hist,
        'time':      elapsed,
        'train_acc': train_acc,
        'model':     model,
    }
    print(f"  {name} → Train Acc: {train_acc:.4f} | Time: {elapsed:.1f}s")

# ── Text generation ───────────────────────────────────────────────────────────
def generate(model, seed_chars, n=80):
    seed_enc = [char2idx[c] for c in seed_chars[-SEQ_LEN:]]
    out = seed_chars
    for _ in range(n):
        x    = np.array([seed_enc])
        pred = model.predict(x, verbose=0)[0]
        pred = pred ** (1/0.8)
        pred = pred / pred.sum()
        nxt  = np.random.choice(len(pred), p=pred)
        out += idx2char[nxt]
        seed_enc = seed_enc[1:] + [nxt]
    return out

seed = TEXT[:SEQ_LEN]
print("\n" + "=" * 60)
print("TEXT GENERATION COMPARISON")
print("=" * 60)
for name, res in results.items():
    gen = generate(res['model'], seed)
    print(f"\n{name}:\n  {gen}")

# ── Summary Table ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print(f"{'Model':<12} {'Accuracy':>10} {'Time (s)':>12} {'Params':>12}")
print("-" * 60)
params = {'SimpleRNN': rnn_params, 'LSTM': lstm_params, 'GRU': gru_params}
for name, res in results.items():
    print(f"{name:<12} {res['train_acc']:>10.4f} {res['time']:>12.1f} {params[name]:>12,}")

# ── Plot ──────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("EXP 9 – GRU vs LSTM vs SimpleRNN", fontsize=14)

# Val loss
ax = axes[0, 0]
for name, res in results.items():
    ax.plot(res['history'].history['val_loss'], label=name)
ax.set_title("Validation Loss")
ax.set_xlabel("Epoch"); ax.set_ylabel("Loss")
ax.legend(); ax.grid(True)

# Val accuracy
ax = axes[0, 1]
for name, res in results.items():
    ax.plot(res['history'].history['val_accuracy'], label=name)
ax.set_title("Validation Accuracy")
ax.set_xlabel("Epoch"); ax.set_ylabel("Accuracy")
ax.legend(); ax.grid(True)

# Training time bar
ax = axes[1, 0]
names  = list(results.keys())
times  = [results[n]['time'] for n in names]
colors = ['steelblue', 'orange', 'green']
bars   = ax.bar(names, times, color=colors)
for bar, t in zip(bars, times):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f"{t:.1f}s", ha='center', fontsize=10)
ax.set_title("Training Time (seconds)")
ax.set_ylabel("Time (s)"); ax.grid(True, axis='y')

# Parameter count bar
ax = axes[1, 1]
param_vals = [params[n] for n in names]
bars = ax.bar(names, param_vals, color=colors)
for bar, p in zip(bars, param_vals):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50,
            f"{p:,}", ha='center', fontsize=9)
ax.set_title("Model Parameters")
ax.set_ylabel("# Parameters"); ax.grid(True, axis='y')

plt.tight_layout()
plt.savefig("exp9_gru_results.png", dpi=120)
plt.show()
print("\nPlot saved: exp9_gru_results.png")
