# solution 1 (BFS)
# import sys
# from collections import deque
# input = sys.stdin.readline
# N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1 ,-1]
# n_regions = []
# _max = 0

# for i in range(N):
#     for j in range(N):
#         _max = max(_max, graph[i][j])

# def bfs(i, j, k):
#     queue = deque()
#     queue.append([i, j])
#     count = 1
#     while queue:
#         x, y = queue.popleft()
#         visited[x][y] = 1
#         for i in range(4):
#             nx = dx[i] + x
#             ny = dy[i] + y
#             if 0<= nx < N and 0<= ny < N:
#                 if graph[nx][ny] > k and visited[nx][ny] == 0:
#                     visited[nx][ny] = 1
#                     queue.append([nx,ny])
#                     count += 1
#     return count

# result = 0
# for k in range(_max+1):
#     visited = [[0] * N for _ in range(N)]
#     n_regions = []
#     for i in range(N):
#         for j in range(N):
#             if graph[i][j] > k and visited[i][j] == 0:
#                 n_regions.append(bfs(i, j, k))
#     result = max(result, len(n_regions))

# print(result)

# solution 2 (DFS)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(i, j, height):
    for _ in range(4):
        nx = i + dx[_]
        ny = j + dy[_]
        if 0<= nx < N and 0<= ny < N:
            if graph[nx][ny] > height and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx, ny, height)

result = 0
for height in range(max(map(max, graph))):
    count = 0
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] > height and visited[i][j] == 0:
                visited[i][j] = 1
                count += 1
                dfs(i, j, height)

    result = max(result, count)
print (result)

# Failed solution
# import sys
# from collections import deque
# input = sys.stdin.readline
# N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]

# def bfs(height: int) -> int:
#     count = 0
#     visited = [[0] * N for _ in range(N)]
#     queue = deque()
#     for i in range(N):
#         for j in range(N):
#             if graph[i][j] > height:
#                 visited[i][j] = 1
    
#     for i in range(N):
#         for j in range(N):
#             if visited[i][j] == 1:
#                 queue.append([i, j])
#                 count += 1
#                 while queue:
#                     x, y = queue.popleft()
#                     if visited[x][y] == 1:
#                         visited[x][y] += 1
#                     for k in range(4):
#                         nx = x + dx[k]
#                         ny = y + dy[k]
#                         if 0<= nx < N and 0<= ny < N:
#                             if visited[nx][ny] == 1:
#                                 visited[nx][ny] += 1
#                                 queue.append([nx, ny])
#     return count
            
# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1 ,-1]
# n_regions = []
# for height in range(1, 100+1):
#     n_regions.append(bfs(height))
# print (max(n_regions))


