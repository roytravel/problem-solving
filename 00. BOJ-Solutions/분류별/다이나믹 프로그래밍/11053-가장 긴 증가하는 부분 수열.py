import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

LIS = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            LIS[i] = max(LIS[i], LIS[j]+1)
print (max(LIS))


# 한 수열에서 여러 개의 LIS가 나올 수 있는 것을 고려하지 못한 코드
# length = 0
# temp = 0
# for i in A:
#     if i > temp:
#         temp = i
#         length += 1
# print (length)