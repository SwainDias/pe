# Q6. Ambiguity Detection
# Classify sentence as Syntactic or Semantic ambiguity
#
# True automated detection needs a full parser + semantic DB (not available here).
# Best we can do without those:
#   - Semantic:  check if any word in the sentence has multiple known meanings
#   - Syntactic: check if the sentence matches known ambiguous structural patterns
# For anything not caught by rules, we fall back to a hardcoded lookup.

# Words known to have multiple meanings (homonyms / polysemous words)
ambiguous_words = {
    "bank", "duck", "bat", "bark", "fly", "light", "match",
    "rock", "spring", "crane", "date", "fair", "letter", "right",
    "saw", "scale", "suit", "tie", "watch", "well"
}

# Patterns that commonly cause syntactic ambiguity
# (simplified: prepositional phrase attachment, gerund subject/verb)
syntactic_patterns = [
    "with",        # PP attachment:  "I saw the man with the telescope"
    "flying",      # gerund:         "flying planes can be dangerous"
    "old men and women",  # coordination scope
]

def detect_ambiguity(sentence):
    words = sentence.lower().split()
    lower = sentence.lower()

    # Check syntactic patterns first (structural ambiguity takes priority)
    for pattern in syntactic_patterns:
        if pattern in lower:
            return "Syntactic Ambiguity", "Contains pattern '" + pattern + "' which allows multiple parse trees"

    # Check for semantic ambiguity (word with multiple meanings)
    for word in words:
        clean_word = word.strip(".,!?")
        if clean_word in ambiguous_words:
            return "Semantic Ambiguity", "Word '" + clean_word + "' has multiple meanings"

    return "Unknown", "Cannot determine automatically"

# Test sentences
sentences = [
    "I saw the man with the telescope",
    "The bank was steep",
    "Flying planes can be dangerous",
    "He saw her duck",
    "I watched the match",
]

for sentence in sentences:
    ambiguity_type, reason = detect_ambiguity(sentence)
    print("Sentence :", sentence)
    print("Type     :", ambiguity_type)
    print("Reason   :", reason)
    print()



#OR

import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Run once
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Convert NLTK POS -> WordNet POS
def wn_pos(tag):
    if tag.startswith('N'):
        return wn.NOUN
    if tag.startswith('V'):
        return wn.VERB
    if tag.startswith('J'):
        return wn.ADJ
    if tag.startswith('R'):
        return wn.ADV
    return None

def semantic_ambiguity(sentence):

    tokens = word_tokenize(sentence)
    tagged = pos_tag(tokens)

    ambiguous = []

    for word, tag in tagged:

        pos = wn_pos(tag)

        if not pos:
            continue

        # meanings for this POS only
        synsets = wn.synsets(word, pos=pos)

        # ambiguous if multiple meanings exist
        if len(synsets) > 1:

            meanings = [s.definition() for s in synsets[:3]]

            ambiguous.append({
                "word": word,
                "meanings": meanings
            })

    return ambiguous


# Test
sentences = [
    "The bank was steep",
    "He saw her duck",
    "I watched the match"
]

for s in sentences:

    print("\nSentence:", s)

    result = semantic_ambiguity(s)

    if result:

        print("Semantic ambiguity detected:\n")

        for item in result:

            print("Word:", item["word"])

            for m in item["meanings"]:
                print(" -", m)

    else:
        print("No ambiguity found")
