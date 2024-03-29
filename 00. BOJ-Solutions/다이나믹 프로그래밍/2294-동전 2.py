import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [10001] * (k + 1)
dp[0] = 0
coins = []
for _ in range(n):
    coins.append(int(input()))

for coin in coins:
    for i in range(1, k+1):
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i-coin]+1)
        
if dp[k] == 10001:
    print (-1)
else:
    print (dp[k])