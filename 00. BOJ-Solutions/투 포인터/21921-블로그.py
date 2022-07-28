# -*- coding:utf-8 -*-
import sys
input = sys.stdin.readline
N, X = map(int, input().split())
visit = list(map(int, input().split()))

if max(visit) == 0:
    print ("SAD")
    exit()

value = sum(visit[:X])
MAX = value
count = 1

for i in range(X, N):
    # 슬라이딩 윈도우: ex) 1 + 4 = 5 --> 5 + 2 = 7 --> 7 - 1 = 6
    value += visit[i] 
    value -= visit[i-X]

    if value > MAX:
        MAX = value
        count = 1

    elif value == MAX:
        count += 1

print (MAX)
print (count)

# time over
# import sys
# input = sys.stdin.readline
# N, X = map(int, input().split())
# visit = list(map(int, input().split()))

# if max(visit) == 0:
#     print ("SAD")
#     exit()

# SUM = []
# for i in range(N):
#     SUM.append(sum(visit[i:i+X]))

# MAX = max(SUM)
# print (MAX)
# print (SUM.count(MAX))