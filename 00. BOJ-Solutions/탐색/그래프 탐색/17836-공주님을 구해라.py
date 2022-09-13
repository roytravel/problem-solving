import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([start])
    visited[0][0] = 1
    result = sys.maxsize
    while queue:
        x, y = queue.popleft()
        if (x, y) == (N-1, M-1):
            return min(visited[x][y]-1, result)

        if castle[x][y] == 2:
            result = visited[x][y]-1 + (N-1-x) + (M-1-y)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if castle[nx][ny] == 0 or castle[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
    return result

N, M, T = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for __ in range(M)] for _ in range(N)]
result = bfs([0, 0])
print ("Fail" if result > T else result)