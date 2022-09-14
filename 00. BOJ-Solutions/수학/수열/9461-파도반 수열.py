import sys
input = sys.stdin.readline
P = [1, 1, 1]
for i in range(100-3):
    P.append(P[i]+P[i+1])

T = int(input())
for _ in range(T):
    N = int(input())
    print (P[N-1])