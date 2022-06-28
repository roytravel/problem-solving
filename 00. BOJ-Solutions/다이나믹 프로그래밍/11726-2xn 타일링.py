import sys
input = sys.stdin.readline

N = int(input())

DP = [0] * (1000 + 1)
DP[1] = 1
DP[2] = 2

for i in range(3, 1000+1):
    DP[i] = DP[i-2] + DP[i-1]

print (DP[N] % 10007)