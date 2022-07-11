import sys
input = sys.stdin.readline
N, K = map(int, input().split())
# solution 1
# stuff = [[0, 0]]
# dp = [[0] * (K+1) for _ in range(N+1)]

# for _ in range(N):
#     W, V = map(int, input().split())
#     stuff.append([W, V])

# for i in range(1, N+1):
#     for j in range(1, K+1):
#         weight = stuff[i][0]
#         value = stuff[i][1]

#         if j < weight:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
        
# print (dp[N][K])

# solution 2
cache = {0:0}
for _ in range(N):
    curr_weight, curr_value = map(int, input().split())
    temp = {}
    for weight, value in cache.items():
        if curr_weight + weight <= K and curr_value + value > cache.get(curr_weight + weight, 0):
            temp[curr_weight + weight] = curr_value + value
            print (True, temp)
    print (False, cache)
    cache.update(temp)
    print (True, cache)

print (cache)
print (max(cache.values()))