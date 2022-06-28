import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = [0] * n
dp[0] = array[0]

for i in range(1, n):
    dp[i] = max(array[i], dp[i-1] + array[i])

print (max(dp))

# 메모리 초과
# import sys
# input = sys.stdin.readline

# n = int(input())
# array = list(map(int, input().split()))
# global_sum = []
# for i in range(n):
#     local_sum = 0
#     for j in range(i, n):
#         local_sum += array[j]
#         global_sum.append(local_sum)
    
# print (max(global_sum))


# 시간 초과 1
# import sys
# input = sys.stdin.readline

# n = int(input())
# array = list(map(int, input().split()))

# global_sum = []
# for i in range(n):
#     local_sum = 0
#     temp = -sys.maxsize
#     for j in range(i, n):
#         local_sum += array[j]
#         if local_sum > temp:
#             temp = local_sum
#             global_sum.append(temp)

# print (max(global_sum))


# 시간 초과 2
# import sys
# input = sys.stdin.readline

# n = int(input())
# array = list(map(int, input().split()))
# LIS = [0] * n

# for i in range(n):
#     local_sum = 0
#     temp = -1001
#     for j in range(i, n):
#         local_sum += array[j]
#         if local_sum > temp:
#             temp = local_sum
#     LIS[i] = temp

# print (max(LIS))


