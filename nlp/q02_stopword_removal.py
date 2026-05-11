# Q2. Stopword Removal (Manual List)

stopwords = [
    "i", "me", "my", "we", "our", "you", "your", "he", "she", "it",
    "the", "a", "an", "and", "or", "but", "is", "are", "was", "were",
    "in", "on", "at", "to", "for", "of", "with", "this", "that", "they"
]

sentence = "The quick brown fox and the lazy dog are sitting in the park"

words = sentence.lower().split()

cleaned_words = []
for word in words:
    if word not in stopwords:
        cleaned_words.append(word)

cleaned_text = " ".join(cleaned_words)

print("Original :", sentence)
print("Cleaned  :", cleaned_text)
