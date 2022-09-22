import sys
from collections import deque
input = sys.stdin.readline

def change():
    flag = False
    for i in range(N):
        for j in range(M):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                flag = True
            elif graph[i][j] == 2:
                graph[i][j] = 1
    return flag

def bfs():
    queue = deque([[0, 0]])
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0:
                if graph[nx][ny] >= 1:
                    graph[nx][ny] += 1
                else:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
while True:
    visited = [[0] * M for _ in range(N)]
    bfs()
    if change():
        answer += 1
    else:
        break
print(answer)

# Wrong.
# import sys
# from collections import deque
# input = sys.stdin.readline 

# def check():
#     for i in range(N):
#         for j in range(M):
#             if graph[i][j] == 1:
#                 return True
#     return False

# def change(one):
#     for i in range(N):
#         for j in range(M):
#             if one[i][j] == 1:
#                 graph[i][j] = 0

# def bfs():
#     one = [[0] * M for _ in range(N)]
#     for x in range(N):
#         for y in range(M):
#             if graph[x][y] == 1:
#                 count = 0
#                 for z in range(4):
#                     nx = x + dx[z]
#                     ny = y + dy[z]
#                     if 0<=nx<N and 0<=ny<M:
#                         if graph[nx][ny] == 0:
#                             count += 1
    
#                         if count >=2:
#                             one[x][y] = True
#                             break
#     return one

# N, M = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]
# answer = 0

# while check():
#     one = bfs()
#     change(one)
#     answer += 1

# print (answer)