import sys
input = sys.stdin.readline
N, M, K = list(map(int, input().split()))
team = 0

# my fault
# intern = 0
# while True:
#     if N//2 >= M:
#         N = N-1
#         intern = intern + 1
#         if K == intern:
#             break
    
#     elif N//2 < M:
#         M = M -1
#         intern = intern + 1
#         if K == intern:
#             break

# t1 = N // 2
# t2 = M 
# print(min(t1, t2))

while True:
    N = N - 2
    M = M - 1
    if N < 0 or M < 0 or (N+M) < K:
        break
    team = team + 1
print (team)