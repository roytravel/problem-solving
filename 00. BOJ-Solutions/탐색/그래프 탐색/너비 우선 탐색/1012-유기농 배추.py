import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b) -> None:
    graph[a][b] = 0
    queue = deque([[a, b]])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny <N:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append([nx, ny])

T = int(input())
for _ in range(T):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    M, N, K = map(int, input().split())
    worm = 0
    graph = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                bfs(i, j)
                worm += 1
    print (worm)
