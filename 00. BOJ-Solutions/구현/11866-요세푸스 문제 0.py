import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
Z = K
circle = [i+1 for i in range(N)]
permutation = []
