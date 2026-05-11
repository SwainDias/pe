# Q4. Morphological Analysis
# Free morpheme  = can stand alone as a word
# Bound morpheme = cannot stand alone, must attach to another morpheme

# word : [ (morpheme, type), ... ]
words = {
    "unhappiness":  [("un-",    "bound"), ("happy",   "free"), ("-ness",  "bound")],
    "replayed":     [("re-",    "bound"), ("play",    "free"), ("-ed",    "bound")],
    "international":[("inter-", "bound"), ("nation",  "free"), ("-al",    "bound")],
}

for word, morphemes in words.items():
    print(word)
    for morpheme, mtype in morphemes:
        print("  ", morpheme, "-", mtype)
    print()

# OR
prefixes = ["un", "re", "inter"]
suffixes = ["ness", "ed", "al"]

def morphological_analysis(word):
    result = []

    # prefix detection
    for p in prefixes:
        if word.startswith(p):
            result.append((p, "bound"))
            word = word[len(p):]
            break

    # suffix detection
    for s in suffixes:
        if word.endswith(s):
            root = word[:-len(s)]

            result.append((root, "free"))
            result.append((s, "bound"))
            return result

    result.append((word, "free"))
    return result


words = ["unhappiness", "replayed", "international"]

for w in words:
    print(w, "->", morphological_analysis(w))
