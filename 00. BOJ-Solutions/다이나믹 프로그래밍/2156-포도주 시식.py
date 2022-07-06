import sys
input = sys.stdin.readline
N = int(input())

wine = []
for i in range(N):
    wine.append(int(input()))

dp = [0] * N
dp[0] = wine[0]

if N > 1:
    dp[1] = wine[0]+wine[1]
if N > 2:
    dp[2] = max(wine[2]+wine[1], wine[2]+wine[0], dp[1])

for i in range(3, N):
    dp[i] = max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], dp[i-2]+wine[i])

print(dp[N-1])


# time over 2
# import sys
# input = sys.stdin.readline

# N = int(input())
# wine = []
# for _ in range(N):
#     wine.append(int(input()))

# dp = [0] * (N+1)
# for i in range(N):
#     cnt = 0
#     for j in range(i, N):
#         if cnt == 2:
#             cnt = 0
#             continue
#         else:
#             dp[i] = max(dp[i], wine[j] + dp[i])
#         cnt +=1

# print (max(dp))

# time over
# import sys
# input = sys.stdin.readline

# N = int(input())
# wine = []
# for _ in range(N):
#     wine.append(int(input()))

# dp = [0] * (N+1)
# for i in range(N):
#     cnt = 0
#     for j in range(N):
#         if cnt == 2:
#             cnt = 0
#             continue
#         else:
#             dp[i] += wine[j]
#         cnt +=1

# print (max(dp))