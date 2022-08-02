from collections import deque

def bfs(start, N, M, maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[0 for _ in range(M)] for __ in range(N)]
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append([nx, ny])
                    visited[nx][ny] = True
    return visited

def solution(maps):
    N, M = len(maps), len(maps[0])
    visited = bfs([0, 0], N, M, maps)
    if visited[N-1][M-1] == False:
        return -1
    return maps[N-1][M-1]