from collections import defaultdict

card = defaultdict(int)
N = int(input())
array1 = list(map(int, input().split()))

M = int(input())
array2 = list(map(int, input().split()))

for n in array1:
    card[n] += 1

for n in array2:
    print (card[n], end=' ')