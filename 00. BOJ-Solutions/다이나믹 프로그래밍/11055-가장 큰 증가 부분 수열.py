import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
DP = A[:]

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            DP[i] = max(DP[i], DP[j] + A[i])

print (max(DP))