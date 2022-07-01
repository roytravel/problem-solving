# # coding:utf-8
# import sys
# from collections import deque
# input = sys.stdin.readline

# box = []
# N = int(input())
# for _ in range(N):
#     box.append(list(map(int, input().split())))

# start = box[0][0]
# right_x, bottom_y = 0, start
# right_y, bottom_x = start, 0

# queue = deque()
# queue.append([right_x, bottom_y])
# queue.append([right_y, bottom_x])
# count = 0
# while queue:
#     x, y = queue.popleft()
#     if box[x][y] == 0 & (x == N-1 and y== N-1):
#         count += 1
#         continue
    
#     # 오른쪽으로 갈 수 있는 경우
#     if box[x][y] + y <= N-1:
#         y = box[x][y] + y
#         queue.append([x, y])
#     # 아래쪽으로 갈 수 있는 경우
#     if box[x][y] + x <= N-1:
#         x = box[x][y] + x
#         queue.append([x, y])

# print (count-1)

import sys
input = sys.stdin.readline

N = int(input())
box = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * N for _ in range(N)]
DP[0][0] = 1

for x in range(N):
    for y in range(N):
        if DP[x][y] !=0 and box[x][y] !=0:
            if box[x][y] + y <= N-1:
                DP[x][y+box[x][y]] += DP[x][y]
            
            if box[x][y] + x <= N-1:
                DP[x+box[x][y]][y] += DP[x][y]

print (DP[N-1][N-1])