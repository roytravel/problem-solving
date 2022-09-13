import math
import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())
day = (V-B) / (A-B)
print (math.ceil(day))

# Solution using binary search: recursive
# import sys
# input = sys.stdin.readline

# def binary_search(start, end):
#     global answer
#     if start <= end:
#         mid = (start+end) // 2
#         y2 = mid * (A - B)
#         y1 = y2 + B
#         if y1 < V:
#             binary_search(mid+1, end)
#         else:
#             answer = mid
#             binary_search(start, mid-1)

# A, B, V = map(int, input().split())
# start, end = 1, (V//(A-B)) + 1 
# y1, y2, mid, answer = 0, 0, 0, 0
# binary_search(start, end)
# print (answer)