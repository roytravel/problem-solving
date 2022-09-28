import sys
sys.setrecursionlimit
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False] * N
array = []

def recursion(start):
    if len(array) == M:
        print(*array)
        return
    used = 0
    for i in range(start, N):
        if not visited[i] and nums[i] != used:
            visited[i] = True
            array.append(nums[i])
            used = nums[i]
            recursion(i+1)
            array.pop()
            visited[i] = False
recursion(0)

# False
# import sys
# sys.setrecursionlimit
# input = sys.stdin.readline

# def recursion(array, depth):
#     if len(array) == M:
#         for i in array:
#             print (i, end=' ')
#         print()
#         return
#     else:
#         for num in nums:
#             if count[num]:
#                 count[num] -= 1
#                 array.append(num)
#                 recursion(array, depth+1)
#                 array.pop()
#                 count[num] += 1

# N, M = map(int, input().split())
# nums = list(map(int, input().split()))
# nums.sort()
# count = [0] *(max(nums)+1)
# for n in nums:
#     count[n] += 1

# recursion([], 0) 