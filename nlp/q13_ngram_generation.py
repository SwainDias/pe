# Q13. Bigram Text Generation

import random
from collections import defaultdict

corpus = "the cat sat on the mat the cat ate the rat the rat sat on the mat"

words = corpus.split()

# Build bigram model: { word: [list of words that follow it] }
bigram_model = defaultdict(list)
for i in range(len(words) - 1):
    bigram_model[words[i]].append(words[i+1])

print("Bigram model:")
for word in bigram_model:
    print(" ", word, "->", bigram_model[word])

# Generate text
def generate(model, seed, length=12):
    result = [seed]
    current = seed
    for _ in range(length - 1):
        next_words = model.get(current)
        if not next_words:
            break
        current = random.choice(next_words)
        result.append(current)
    return " ".join(result)

random.seed(42)
print()
print("Generated text:", generate(bigram_model, "the", 12))
