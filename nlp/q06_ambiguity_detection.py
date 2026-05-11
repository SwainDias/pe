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
