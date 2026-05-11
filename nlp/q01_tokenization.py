# Q1. Tokenization Task
# No external APIs - manual sentence and word splitting

paragraph = "Natural Language Processing is a field of AI. It helps computers understand human language. Many applications use NLP today."


# Split into sentences manually using punctuation markers
sentences = []
current = ""
for char in paragraph:
    current += char
    if char in ".!?":
        sentences.append(current.strip())
        current = ""
if current.strip():
    sentences.append(current.strip())

# Split each sentence into words manually
all_tokens = []
for sentence in sentences:
    # Remove punctuation and split on whitespace
    clean = ""
    for char in sentence:
        if char.isalnum() or char == " ":
            clean += char
        else:
            clean += " "
    words = clean.split()
    all_tokens.extend(words)
    print("Sentence:", sentence)
    print("Words:", words)
    print()

print("Total tokens:", len(all_tokens))