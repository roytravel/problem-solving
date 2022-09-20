import sys
from collections import deque
input = sys.stdin.readline

def get_shortest_dist(start):   
    queue = deque([start])
    while queue:
        x, y, z = queue.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append([nx, ny, 1])
                elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append([nx, ny, z])
    return -1

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
print (get_shortest_dist([0, 0, 0]))