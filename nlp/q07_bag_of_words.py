# Q7. Bag of Words

sentences = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "the cat chased the dog"
]

# Build vocabulary
vocab = []
for sentence in sentences:
    for word in sentence.split():
        if word not in vocab:
            vocab.append(word)
vocab.sort()

print("Vocabulary:", vocab)
print()

# Build BoW matrix
for sentence in sentences:
    row = []
    for word in vocab:
        row.append(sentence.split().count(word))
    print(sentence)
    print(row)
    print()
