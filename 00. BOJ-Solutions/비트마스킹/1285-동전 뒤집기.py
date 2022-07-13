import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
coin_matrix = []
for _ in range(N):
    coin_matrix.append(input().strip())

res = list(permutations(coin_matrix, len(coin_matrix)))
for i in res:
    print (i)