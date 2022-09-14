import sys
from itertools import permutations
input = sys.stdin.readline
L, C = map(int, input().split())
array = map(str, input().split())

permutation = permutations(array, L)
cipher = []
for i in list(permutation):
    cipher.append("".join(i))

cipher.sort()
for i in cipher:
    print (i)
    