# Solution 
import sys
input = sys.stdin.readline
N = int(input())
T = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    for j in range(len(T[i])):
        if j == 0:
            T[i][j] = T[i][j] + T[i-1][j]
        elif i == j:
            T[i][j] = T[i][j] + T[i-1][j-1]
        else:
            T[i][j] = max(T[i-1][j-1], T[i-1][j]) + T[i][j] # Here is where I missed points.
print (max(T[N-1]))


# Wrong... why...
# import sys
# input = sys.stdin.readline
# N = int(input())
# triangle = [list(map(int, input().split())) for _ in range(N)]
# dp = [[0] * (N) for _ in range(N)]
# dp[0][0] = triangle[0][0]
# for i in range(1, N):
#     for j in range(len(triangle[i])):
#         if j == 0:
#             dp[i][j] = max(dp[i-1][j]+triangle[i-1][j], dp[i-1][j]+triangle[i-1][j])
#         elif j == len(triangle[i])-1:
#             dp[i][j] = dp[i-1][j]+triangle[i][j]
#         else:
#             dp[i][j] = max(dp[i-1][j-1]+triangle[i][j], dp[i-1][j+1]+triangle[i][j])
# print (max(dp[-1]))