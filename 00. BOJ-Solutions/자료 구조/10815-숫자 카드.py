import sys
from collections import defaultdict
input = sys.stdin.readline

card = defaultdict(int)

N = int(input())
array1 = list(map(int, input().split()))

M = int(input())
array2 = list(map(int, input().split()))

for n in array1:
    card[n] += 1

for n in array2:
    if card[n]:
        print (1, end=' ')
    else:
        print (0, end=' ')