def chiper(sentence):
	return "".join([ chr(219 - ord(char)) if char.islower() else char for char in sentence])

chipered = chiper("this is a english sentence")
print(chipered)
print(chiper(chipered))