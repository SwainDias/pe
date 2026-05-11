# Q18. RNN Sentiment Analysis on NLTK Movie Reviews

import nltk
nltk.download('movie_reviews', quiet=True)
from nltk.corpus import movie_reviews

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load data
reviews = []
labels  = []
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        reviews.append(movie_reviews.raw(fileid))
        labels.append(1 if category == "pos" else 0)

labels = np.array(labels)

# Tokenize and pad
MAX_VOCAB = 5000
MAX_LEN   = 200

tokenizer = Tokenizer(num_words=MAX_VOCAB, oov_token="<OOV>")
tokenizer.fit_on_texts(reviews)
sequences = tokenizer.texts_to_sequences(reviews)
padded    = pad_sequences(sequences, maxlen=MAX_LEN, padding='post', truncating='post')

# Train/test split (manual, no sklearn needed)
split = int(0.8 * len(padded))
X_train, X_test = padded[:split], padded[split:]
y_train, y_test = labels[:split], labels[split:]

# Build model
model = Sequential([
    Embedding(input_dim=MAX_VOCAB, output_dim=32, input_length=MAX_LEN),
    SimpleRNN(32),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

model.fit(X_train, y_train, epochs=3, batch_size=64, validation_split=0.1)

loss, acc = model.evaluate(X_test, y_test)
print("\nTest accuracy:", round(acc, 4))

# Sample predictions
samples = [
    "This movie was absolutely fantastic and thrilling!",
    "Terrible film, complete waste of time."
]
sample_seq    = tokenizer.texts_to_sequences(samples)
sample_padded = pad_sequences(sample_seq, maxlen=MAX_LEN, padding='post')
preds         = model.predict(sample_padded)

for review, pred in zip(samples, preds):
    print(review, "->", "Positive" if pred[0] >= 0.5 else "Negative", round(float(pred[0]), 4))
