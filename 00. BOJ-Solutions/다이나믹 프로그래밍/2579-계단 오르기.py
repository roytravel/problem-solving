import sys
input = sys.stdin.readline

N = int(input())
stair = [0]
score = 0

for _ in range(N):
    stair.append(int(input()))

if N == 1:
    print(stair[1])

else:
    dp = [0] * (N+1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]

    for i in range(3, N+1):
        case1 = stair[i] + dp[i-2]
        case2 = stair[i] + stair[i-1] + dp[i-3]
        dp[i] = max(case1, case2)
    print (dp[N])