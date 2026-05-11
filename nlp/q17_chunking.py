# Q17. Chunking - Noun Phrase (NP) Identification
# NP rule: DET? ADJ* NOUN
# Since averaged_perceptron_tagger is not guaranteed to be available,
# we use a rule-based POS tagger (same rules as Q5) and then chunk.

sentence = "The quick brown fox jumped over a lazy sleeping dog"

# Rule-based POS tagger (no external data needed)
DET_WORDS  = {"the", "a", "an", "this", "that", "these", "those"}
ADJ_SUFFIX = ("ful", "ous", "ive", "al", "ic", "ble", "ing")  # "ing" covers sleeping, running etc.
NOUN_WORDS = {"fox", "dog", "cat", "mat", "park", "man", "woman", "city", "tree"}
VERB_WORDS = {"jumped", "ran", "sat", "chased", "is", "are", "was", "were", "over"}

def pos_tag(word):
    w = word.lower()
    if w in DET_WORDS:  return "DET"
    if w in VERB_WORDS: return "VERB"
    if w in NOUN_WORDS: return "NOUN"
    if w.endswith(ADJ_SUFFIX): return "ADJ"
    if w.endswith("ly"): return "ADV"
    return "NOUN"  # default unknown words to NOUN

tokens = sentence.split()
tagged = [(word, pos_tag(word)) for word in tokens]

print("POS Tags:")
for word, tag in tagged:
    print(" ", word, "->", tag)

# Chunking: find NP = DET? ADJ* NOUN
print("\nNoun Phrases (NP):")
i = 0
while i < len(tagged):
    chunk = []
    j = i
    # optional DET
    if tagged[j][1] == "DET":
        chunk.append(tagged[j][0])
        j += 1
    # zero or more ADJ
    while j < len(tagged) and tagged[j][1] == "ADJ":
        chunk.append(tagged[j][0])
        j += 1
    # required NOUN
    if j < len(tagged) and tagged[j][1] == "NOUN":
        chunk.append(tagged[j][0])
        print("  NP:", chunk)
        i = j + 1
    else:
        i += 1
