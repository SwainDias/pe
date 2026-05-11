sentences = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "the cat chased the dog"
]

# Step 1: Build vocabulary
vocab = []

for sentence in sentences:
    words = sentence.split()

    for word in words:
        if word not in vocab:
            vocab.append(word)

vocab.sort()

print("Vocabulary:")
print(vocab)
print()

# Step 2: Build Bag of Words matrix

for sentence in sentences:

    words = sentence.split()

    row = []

    for vocab_word in vocab:

        count = 0

        for word in words:
            if word == vocab_word:
                count += 1

        row.append(count)

    print("Sentence:", sentence)
    print("BoW Row :", row)
    print()
