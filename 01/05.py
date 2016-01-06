def char_n_gram(sentence, n):
    return [sentence[index:index+n] for index in range(len(sentence))]

def word_n_gram(sentence, n):
    words = sentence.split()
    return [words[index:index+n] for index in range(len(words))]

sentence = "I am an NLPer"
print(char_n_gram(sentence, 2))
print(word_n_gram(sentence, 2))