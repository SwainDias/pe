# Q5. Part-of-Speech Tagging (Rule-based)
# No external taggers - uses only word-lists and suffix rules

determiners  = {"the", "a", "an", "this", "that", "these", "those", "my", "your"}
conjunctions = {"and", "or", "but", "so", "yet", "nor"}
prepositions = {"in", "on", "at", "to", "for", "of", "with", "by", "from", "over"}
pronouns     = {"i", "he", "she", "it", "they", "we", "you", "me", "him", "her"}
be_verbs     = {"is", "are", "was", "were", "am", "be", "been", "being"}

def pos_tag(word):
    w = word.lower()
    if w in determiners:   return "DET"
    if w in conjunctions:  return "CONJ"
    if w in prepositions:  return "PREP"
    if w in pronouns:      return "PRON"
    if w in be_verbs:      return "VERB"
    if w.endswith("ly"):   return "ADV"
    if w.endswith("ing") or w.endswith("ed"): return "VERB"
    if w.endswith("tion") or w.endswith("ness") or w.endswith("ment"): return "NOUN"
    if w.endswith("ful") or w.endswith("ous") or w.endswith("ive"):    return "ADJ"
    return "NOUN"  # default

sentence = "The quick fox jumped over the lazy dog and ran quickly"

for word in sentence.split():
    print(word, "-->", pos_tag(word))
