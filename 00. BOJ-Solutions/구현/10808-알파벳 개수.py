from collections import defaultdict
word = input()
alphabet = defaultdict(int)

for c in word:
    n = ord(c)-97
    alphabet[n] += 1

for i in range(26):
    print (alphabet[i], end = ' ')