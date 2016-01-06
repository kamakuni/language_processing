def ngram(word, n):
    return [word[index:index+n] for index in range(len(word))]

word1 = "paraparaparadise"
word2 = "paragraph"
X = set(ngram(word1,2))
Y = set(ngram(word2,2))

print(X.union(Y))
print(X.intersection(Y))
print(X.difference(Y))

print("se" in X)
print("se" in Y)