import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coin = []
for _ in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)
dp = [0] * N
for i in range(len(coin)):
    if K % coin[i] == 0: # 최대값으로 coin이 나눠지는 경우는 몫이 최대값이 됨
        dp[i] = max(dp[i], K // coin[i])
    else: #최대값으로 coin이 나눠지지 않는 경우는 나눌 수 있는 최대 크기만큼 나누고 줄여가봐야함
        Q, R = divmod(K, coin[i])
        if R in coin:
            
