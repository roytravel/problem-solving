# -*- coding:utf-8 -*-
# reference: https://hongcoding.tistory.com/14
import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
stack = [0]

# Solution 1
def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        print (start, end, mid)

        if stack[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    print (start, end)
    return start

for i in A:
    if stack[-1] < i:
        stack.append(i)
    else:
        stack[binary_search(i, 0, len(stack)-1)] = i

print (len(stack)-1)


# Solution 2
# for i in A:
#     if stack[-1] < i:
#         stack.append(i)
#     else:
#         stack[bisect_left(stack, i)] = i
    
# print (len(stack)-1)

# Wrong solution 1
# max_value = 0
# count = 0

# for i in range(N):
#     if A[i] > max_value:
#         max_value = A[i]
#         count += 1
# print (count)


# Wrong solution 2
# dp = [1] * N
# for i in range(1, N):
#     for j in range(i):
#         if A[j] < A[i]:
#             dp[i] = max(dp[i], dp[j]+1)
# print (dp)