import sys
input = sys.stdin.readline
N = int(input())

words = []
for _ in range(N):
    words.append(input().strip('\n'))

words = list(set(words))
words.sort(key=lambda x: (len(x), x))
for i in words:
    print (i)