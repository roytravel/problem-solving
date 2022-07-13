import sys
input = sys.stdin.readline
N = int(input())

point = []

for _ in range(N):
    point.append(list(map(int, input().split()))) # x = 현재 위치 y = 목표 위치

for i in point:
    src, dst = i[0], i[1] # x, y
    
    distance = dst - src
    k = -1
    for j in range(0, distance, k):