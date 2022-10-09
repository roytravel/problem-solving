import sys
input = sys.stdin.readline

def dfs(x, y, k):
    if k == K:
        if (x, y) == (0, M-1):
            global count
            count += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] != "T":
                graph[nx][ny] = "T"
                dfs(nx, ny, k+1)
                graph[nx][ny] = "."
N, M, K = map(int, input().split())
dx = [-1, 1, 0, 0] # top, bottom, right, left
dy = [0, 0, 1, -1]
graph = [list(input()) for _ in range(N)]
graph[N-1][0] = "T"
count = 0
dfs(N-1, 0, 1)
print (count)