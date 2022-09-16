# The solution, but solve it again.
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
i, j, size_shark = 0, 0, 2
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def get_shark_pos() -> list:
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                return [i, j]

def eat_fish(a, b, size_shark) -> list:
    dist = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    visited[a][b] = True
    queue = deque([[a, b]])
    shark = []
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == False:
                if graph[nx][ny] <= size_shark:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
                    if graph[nx][ny] < size_shark and graph[nx][ny] != 0:
                        shark.append([nx, ny, dist[nx][ny]])
    return sorted(shark, key=lambda x: (-x[2], -x[0], -x[1]))

eat = 0
time = 0
i, j = get_shark_pos()

while True:
    shark = eat_fish(i, j, size_shark)
    if not shark: # request help to mom.
        break

    nx, ny, dist = shark.pop()
    time += dist

    graph[i][j], graph[nx][ny] = 0, 0
    i, j = nx, ny
    eat += 1
    if eat == size_shark:
        size_shark += 1
        eat = 0
    
print(time)