#!/usr/bin/env python
# -+- coding: utf-8 -+-
word1 = u"パトカー"
word2 = u"タクシー"

result = []
for char1,char2 in zip(word1, word2):
	result += char1 + char2
print("".join([char1+char2 for char1,char2 in zip(word1, word2)]))

#print("".join([char1+char2 for char1,char2 in zip(word1, word2)])