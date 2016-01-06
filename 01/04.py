sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = sentence.split()
result = {}
for index,word in enumerate(words):
    length = 1 if index + 1 in [1, 5, 6, 7, 8, 9, 15, 16, 19] else 2
    result[word[:length]] = index
print(result)