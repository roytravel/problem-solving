import sys
input = sys.stdin.readline
N, M = map(int, input().split())
Q, R = divmod(N, M)
print (Q)
print (R)