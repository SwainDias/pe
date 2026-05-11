# Q16. Context-Free Grammar (CFG) Parsing
# Version 1: Using NLTK
# Version 2: From scratch (recursive descent parser)

# =============================================
# VERSION 1 - NLTK ChartParser
# =============================================

import nltk
nltk.download('punkt', quiet=True)

grammar = nltk.CFG.fromstring("""
    S   -> NP VP
    NP  -> DET N | DET ADJ N | N
    VP  -> V NP | V
    DET -> 'the' | 'a'
    ADJ -> 'big' | 'small' | 'quick' | 'lazy'
    N   -> 'dog' | 'cat' | 'fox' | 'mat'
    V   -> 'sat' | 'chased' | 'saw' | 'jumped'
""")

parser = nltk.ChartParser(grammar)

test_sentences = [
    ["the", "dog", "sat"],
    ["a", "big", "cat", "chased", "the", "dog"],
    ["dog", "the", "sat"],
]

print("=== NLTK ChartParser ===")
for tokens in test_sentences:
    trees = list(parser.parse(tokens))
    if trees:
        print("VALID   :", tokens)
        trees[0].pretty_print()
    else:
        print("INVALID :", tokens)

# =============================================
# VERSION 2 - Recursive Descent Parser (from scratch)
# Grammar:
#   S   -> NP VP
#   NP  -> DET N | DET ADJ N | N
#   VP  -> V NP | V
# =============================================

DET  = {"the", "a"}
ADJ  = {"big", "small", "quick", "lazy"}
N    = {"dog", "cat", "fox", "mat"}
V    = {"sat", "chased", "saw", "jumped"}

def match(tokens, pos, word_set):
    if pos < len(tokens) and tokens[pos] in word_set:
        return pos + 1
    return None

def parse_NP(tokens, pos):
    # DET ADJ N
    p = match(tokens, pos, DET)
    if p is not None:
        p2 = match(tokens, p, ADJ)
        if p2 is not None:
            p3 = match(tokens, p2, N)
            if p3 is not None:
                return p3
        # DET N
        p2 = match(tokens, p, N)
        if p2 is not None:
            return p2
    # N alone
    p = match(tokens, pos, N)
    if p is not None:
        return p
    return None

def parse_VP(tokens, pos):
    p = match(tokens, pos, V)
    if p is None:
        return None
    # V NP
    p2 = parse_NP(tokens, p)
    if p2 is not None:
        return p2
    # V alone
    return p

def parse_S(tokens):
    p = parse_NP(tokens, 0)
    if p is None:
        return False
    p = parse_VP(tokens, p)
    if p is None:
        return False
    return p == len(tokens)  # all tokens consumed

print("\n=== Recursive Descent Parser (from scratch) ===")
for tokens in test_sentences:
    result = "VALID" if parse_S(tokens) else "INVALID"
    print(result, ":", tokens)
