# Q8. TF-IDF Calculation (Manual)
# TF(t, d)  = count of t in d / total words in d
# IDF(t)    = log( N / number of docs containing t )
# TF-IDF    = TF * IDF

import math

documents = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "the cat chased the dog"
]

N = len(documents)

# Build vocabulary
vocab = []
for doc in documents:
    for word in doc.split():
        if word not in vocab:
            vocab.append(word)

# Compute TF for each document
def compute_tf(doc):
    words = doc.split()
    tf = {}
    for word in words:
        tf[word] = tf.get(word, 0) + 1
    for word in tf:
        tf[word] = tf[word] / len(words)
    return tf

# Compute IDF for each word
def compute_idf(word, docs):
    count = 0
    for doc in docs:
        if word in doc.split():
            count += 1
    return math.log(N / count)

tf_list = []
for doc in documents:
    tf_list.append(compute_tf(doc))

print("TF-IDF values:\n")
print("Word".ljust(12), end="")
for i in range(N):
    print(("Doc" + str(i+1)).ljust(10), end="")
print()

for word in vocab:
    idf = compute_idf(word, documents)
    print(word.ljust(12), end="")
    for tf in tf_list:
        tfidf = tf.get(word, 0) * idf
        print(str(round(tfidf, 4)).ljust(10), end="")
    print()
