# coding:utf-8
import sys
from collections import deque
input = sys.stdin.readline

result = sys.maxsize
def bfs(start):
    sword = False
    queue = deque([start])
    while queue:
        x, y, t = queue.popleft()
        if x == N-1 and y == M-1:
            result = min(result, t)
            break
        if t + 1 > T:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if castle[nx][ny] == 1:
                    continue

                elif castle[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append([nx, ny, t+1])
                else:
                    visited[nx][ny] = True
                    temp = t + 1 + abs(nx-(N-1)) + abs(ny-(M-1))
                    if temp <= T:
                        result=temp
                
N, M, T = map(int, input().split())
castle = []
for i in range(N):
    castle.append(list(map(int, input().split())))
visited = [[0 for i in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
bfs([0, 0, 0])

if result > T:
    print ("Fail")
else:
    print (result)

# 맵을 움직인다.

# 칼이 없으면 벽을 지나가야 한다.

# 칼이 있으면 벽을 뚫고갈수 있다.

# 칼이 있는 경우와 없는 경우 중 더 은 거리 선택
    