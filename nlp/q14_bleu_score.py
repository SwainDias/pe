# Q14. BLEU Score (Manual)
# BLEU = BP * exp( sum of w_n * log(p_n) for n=1..4 )
# BP   = 1 if len(candidate) >= len(reference), else exp(1 - len(ref)/len(cand))

import math
from collections import Counter

reference = "the cat sat on the mat"
candidate = "the cat is on the mat"

ref  = reference.split()
cand = candidate.split()

def ngram_precision(ref, cand, n):
    cand_ngrams = [tuple(cand[i:i+n]) for i in range(len(cand)-n+1)]
    ref_ngrams  = [tuple(ref[i:i+n])  for i in range(len(ref)-n+1)]
    cand_count  = Counter(cand_ngrams)
    ref_count   = Counter(ref_ngrams)
    clipped     = sum(min(cand_count[ng], ref_count[ng]) for ng in cand_count)
    return clipped / len(cand_ngrams) if cand_ngrams else 0

# Brevity Penalty
if len(cand) >= len(ref):
    BP = 1.0
else:
    BP = math.exp(1 - len(ref) / len(cand))

# Weighted log sum over 4 n-gram levels
log_sum = 0
for n in range(1, 5):
    p = ngram_precision(ref, cand, n)
    print(str(n) + "-gram precision:", round(p, 4))
    if p > 0:
        log_sum += 0.25 * math.log(p)

bleu = BP * math.exp(log_sum)

print()
print("BP   :", BP)
print("BLEU :", bleu)
