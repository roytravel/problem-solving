import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
time = []
cost = []

for _ in range(N):
    t, c = map(int, input().split())
    time.append(t)
    cost.append(c)

M = 0
for i in range(N):
    M = max(M, dp[i])
    if i + time[i] > N:
        continue
    dp[i+time[i]] = max(dp[i+time[i]], M + cost[i])

print (max(dp))