import sys
input = sys.stdin.readline
C, N = map(int, input().split())
information = []
dp = [sys.maxsize] * (C + 100)
dp[0] = 0

for _ in range(N):
    cost, customer = map(int, input().split())
    information.append([cost, customer])

information.sort(key=lambda x: x[0])

for cost, customer in information:
    for i in range(customer, C+100):
        dp[i] = min(dp[i], dp[i-customer] + cost)
    
print (min(dp[C:]))