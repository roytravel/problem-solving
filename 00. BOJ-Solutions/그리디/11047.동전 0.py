import sys
input = sys.stdin.readline
N, K = map(int, input().split())
cnt = 0
coins = []

# my solution
for _ in range(N):
    coins.append(int(input()))

coins.reverse()
_sum = 0

for coin in coins:
    if coin > K:
        continue
    
    while True:
        _sum = _sum + coin
        cnt = cnt + 1
        if _sum > K:
            _sum = _sum - coin
            cnt = cnt -1
            break
    if _sum == K:
        print(cnt)
        break
    
# others solution
# coins = sorted([int(input()) for i in range(N)], reverse=True)
# for i in range(N):
#     cnt += K // coins[i]
#     K = K % coins[i]
# print (cnt)