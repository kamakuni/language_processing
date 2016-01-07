import random

sentence ="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = sentence.split()
result = []
for word in words:
    if len(word) <= 4:
        pass
    else:
        head = word[0] 
        mid_chars = list(word[1:len(word)-1])
        random.shuffle(mid_chars)
        mid = "".join(mid_chars)
        tail = word[-1]
        word = head + mid + tail
    result.append(word)
print(result)