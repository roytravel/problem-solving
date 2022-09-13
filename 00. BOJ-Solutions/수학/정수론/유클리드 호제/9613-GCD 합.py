import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())

def GCD(A, B):
    if A < B:
        temp = A
        A = B
        B = temp
    while B:
        A, B = B, A % B
    return A

for _ in range(N):
    A = list(map(int, input().split()))[1:]
    combination = combinations(A, 2)
    SUM = []
    for idx in list(combination):
        SUM.append(GCD(idx[0], idx[1]))
    print (sum(SUM))