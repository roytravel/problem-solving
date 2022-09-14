# Solution 2
import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j, color, visited, blind=False):
    queue = deque([[i, j]])
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if not visited[nx][ny]:
                    if not blind:
                        if graph[nx][ny] == color:
                            visited[nx][ny] = True
                            queue.append([nx, ny])
                    else:
                        if color == "R" or color == "G":
                            if graph[nx][ny] == "R" or graph[nx][ny] == "G":
                                visited[nx][ny] = True
                                queue.append([nx, ny])
                        else:
                            if graph[nx][ny] == color:
                                visited[nx][ny] = True
                                queue.append([nx, ny])


def get_color_count(flag):
    visited = [[False for _ in range(N)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == "R" and not visited[i][j]:
                bfs(i, j, "R", visited, flag)
                count += 1

            elif graph[i][j] == "G" and not visited[i][j]:
                bfs(i, j, "G", visited, flag)
                count += 1
            
            elif graph[i][j] == "B" and not visited[i][j]:
                bfs(i, j, "B", visited, flag)
                count += 1

    return count

N = int(input())
graph = [list(input()) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

print (get_color_count(False), get_color_count(True))


# Solution
# import sys
# from collections import deque
# input = sys.stdin.readline

# N = int(input())
# graph = [list(input()) for _ in range(N)]

# def bfs(i, j, color, blind=False):
#     queue = deque([[i, j]])
#     visited[i][j] = True
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<N and 0<=ny<N:
#                 if not visited[nx][ny]:
#                     if not blind:
#                         if graph[nx][ny] == color:
#                             visited[nx][ny] = True
#                             queue.append([nx, ny])
#                     else:
#                         if color == "R" or color == "G":
#                             if graph[nx][ny] == "R" or graph[nx][ny] == "G":
#                                 visited[nx][ny] = True
#                                 queue.append([nx, ny])
#                         else:
#                             if graph[nx][ny] == color:
#                                 visited[nx][ny] = True
#                                 queue.append([nx, ny])


# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]
# visited = [[False for _ in range(N)] for _ in range(N)]
# count = 0
# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == "R" and not visited[i][j]:
#             bfs(i, j, "R")
#             count += 1

#         elif graph[i][j] == "G" and not visited[i][j]:
#             bfs(i, j, "G")
#             count += 1
        
#         elif graph[i][j] == "B" and not visited[i][j]:
#             bfs(i, j, "B")
#             count += 1


# visited = [[False for _ in range(N)] for _ in range(N)]
# blind = 0
# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == "R" and not visited[i][j]:
#             bfs(i, j, "R", True)
#             blind += 1

#         elif graph[i][j] == "G" and not visited[i][j]:
#             bfs(i, j, "G", True)
#             blind += 1
        
#         elif graph[i][j] == "B" and not visited[i][j]:
#             bfs(i, j, "B", True)
#             blind += 1

# print (count, blind)