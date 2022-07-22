# import sys
# input = sys.stdin.readline
# L = int(input())
# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())
# day = 0
# while A > 0 or B > 0:
#     A = A - C
#     B = B - D
#     day += 1
# print (L-day)

n, d = [int(input()) for _ in range(5)], 0
while n[1] > 0 or n[2] > 0: n[1], n[2], d = n[1] - n[3], n[2] - n[4], d+1 
print (n[0]-d)