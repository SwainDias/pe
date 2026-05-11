# Q9. Cosine Similarity (Manual Calculation)
# cosine_similarity = dot(A, B) / ( ||A|| * ||B|| )

import math

A = [1, 2, 3, 4]
B = [4, 3, 2, 1]

dot_product = sum(A[i] * B[i] for i in range(len(A)))
norm_A = math.sqrt(sum(x*x for x in A))
norm_B = math.sqrt(sum(x*x for x in B))

cosine_similarity = dot_product / (norm_A * norm_B)

print("A =", A)
print("B =", B)
print("Dot product =", dot_product)
print("||A|| =", round(norm_A, 4))
print("||B|| =", round(norm_B, 4))
print("Cosine Similarity =", round(cosine_similarity, 4))
