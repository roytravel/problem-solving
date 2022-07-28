import sys
input = sys.stdin.readline
M, N = map(int, input().split())
net = [False, False] + [True] * (N-1)
prime = []
for i in range(2, N+1):
    if net[i]:
        prime.append(i)
        for j in range(2*i, N+1, i):
            net[j] = False

for i in prime:
    if M <= i <=N:
        print (i)

# brute force
# import sys
# import math
# input = sys.stdin.readline

# def is_prime(num):
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True

# N, M = map(int, input().split())
# for i in range(N, M+1):
#     result = is_prime(i)
#     if result:
#         print (i)