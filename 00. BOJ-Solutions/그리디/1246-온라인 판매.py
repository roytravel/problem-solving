import sys
input = sys.stdin.readline
N, M = map(int, input().split())
prices = [int(input()) for _ in range(M)]
prices.sort()
profit, target = 0, 0
for i in range(M):
    egg = min(M-i, N)
    if profit < prices[i] * egg:
        profit = prices[i] * egg
        target = prices[i]
print(target, profit)