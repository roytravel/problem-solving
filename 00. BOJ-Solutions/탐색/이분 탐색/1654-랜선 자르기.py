import sys
input = sys.stdin.readline

N, K = map(int, input().split())
LAN = []
for _ in range(N):
    LAN.append(int(input()))

start, end = 1, max(LAN)
while start <= end:
    mid = (start+end) // 2
    answer = 0
    for L in LAN:
        answer += L // mid
    if answer >= K:
        start = mid + 1
    else:
        end = mid - 1

print (end)


# Time over 
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# LAN = []
# for _ in range(N):
#     LAN.append(int(input()))

# S = sum(LAN) // K
# for num in range(S+1, -1, -1):
#     answer = 0
    
#     for l in LAN:
#         answer += l // num
    
#     if answer >= K:
#         print (num)
#         break