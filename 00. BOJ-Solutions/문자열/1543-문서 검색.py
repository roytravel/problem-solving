import sys
input = sys.stdin.readline

document = input().strip()
word = input().strip()
count = 0
i = 0

while i <= len(document) - len(word):
    if document[i:i+len(word)] == word:
        count += 1
        i += len(word)
    else:
        i += 1
print (count)