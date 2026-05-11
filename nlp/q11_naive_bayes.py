# Q11. Naive Bayes Classification
# P(class | sentence) ∝ P(class) * product of P(word | class) for each word
# Using log probabilities to avoid underflow

import math

# P(word | class)
word_probs = {
    "good":      {"positive": 0.4,  "negative": 0.1},
    "bad":       {"positive": 0.1,  "negative": 0.4},
    "movie":     {"positive": 0.3,  "negative": 0.3},
    "not":       {"positive": 0.1,  "negative": 0.2},
    "excellent": {"positive": 0.3,  "negative": 0.05},
}

# Prior probabilities
P_class = {"positive": 0.5, "negative": 0.5}

test_sentence = "good movie excellent"

log_prob = {"positive": math.log(P_class["positive"]),
            "negative": math.log(P_class["negative"])}

for word in test_sentence.split():
    if word in word_probs:
        print(word, "-> P(pos):", word_probs[word]["positive"], " P(neg):", word_probs[word]["negative"])
        log_prob["positive"] += math.log(word_probs[word]["positive"])
        log_prob["negative"] += math.log(word_probs[word]["negative"])

print()
print("log P(positive):", round(log_prob["positive"], 4))
print("log P(negative):", round(log_prob["negative"], 4))

if log_prob["positive"] > log_prob["negative"]:
    print("Predicted class: positive")
else:
    print("Predicted class: negative")
