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
