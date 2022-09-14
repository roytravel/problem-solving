import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append([nx, ny])
                re[nx][ny] = re[x][y] + 1

N, M = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0] * M for _ in range(N)]
re = [[-1] * M for _ in range(N)]

for i in range(N):
    graph.append(list(map(int, input().split())))

queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            queue.append([i, j])
            visited[i][j] = True
            re[i][j] = 0
        elif graph[i][j] == 0:
            re[i][j] = 0

bfs()

for i in range(N):
    print (*re[i])


# I think this is right answer I don't know Why Is It W R O N G.
# import sys
# from collections import deque
# input = sys.stdin.readline

# def bfs(start):
#     queue = deque(start)
#     flag = True
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<N and 0<=ny<M:
#                 if graph[nx][ny] != 2 and graph[nx][ny] != 0 and visited[nx][ny] != 1:
#                     if flag:
#                         graph[nx][ny] += graph[x][y] -2
#                     else:
#                         graph[nx][ny] += graph[x][y]
#                     visited[nx][ny] = 1
#                     queue.append([nx, ny])
#         flag = False
#     graph[start[0][0]][start[0][1]] = 0

# N, M = map(int, input().split())
# graph = []
# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]
# visited = [[-1] * M for _ in range(N)]

# for i in range(N):
#     graph.append(list(map(int, input().split())))

# target = []
# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 2:
#             target.append([i, j])

# bfs(target)

# for i in range(N):
#     print (*graph[i])