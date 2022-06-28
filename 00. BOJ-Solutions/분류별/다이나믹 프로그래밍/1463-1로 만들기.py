import sys
input = sys.stdin.readline

N = int(input())

DP = [0] * (N + 1)
DP[0], DP[1] = 0, 0
# DP[2] = 1 # DP[3] = 1 # DP[4] = 2
# DP[5] = 3 # DP[6] = 2 # DP[7] = 3
# DP[8] = 3 # DP[9] = 2 # DP[10] = 3
for i in range(2, N+1):
    DP[i] = DP[i-1] + 1

    if i % 3 == 0:
        DP[i] = min(DP[i], DP[i // 3] + 1)
    
    if i % 2 == 0:
        DP[i] = min(DP[i], DP[i // 2] + 1)
    
print(DP[N])

# cnt = 0
# while (N != 1):
#     if N % 3 == 0:
#         N = N / 3
#         cnt += 1
    
#     elif N % 2 == 0:
#         N = N / 2
#         cnt += 1
    
#     else:
#         N = N - 1
#         cnt += 1

# print (cnt)