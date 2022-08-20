from collections import deque

# def minimumMoves(grid, startX, startY, goalX, goalY):
#     count = [[0]*n for _ in range(n)]
#     visit = [[0]*n for _ in range(n)]
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     queue = deque([[startX, startY]])
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<= nx <n and 0<=ny<n and visit[nx][ny] == False:
#                 if grid[nx][ny] == ".":
#                     count[nx][ny] = count[x][y]+1
#                     visit[nx][ny] = True
#                     queue.append([nx, ny])
#     return count[goalX][goalY]


def minimumMoves(grid, startX, startY, goalX, goalY):
    MAX = n*n
    graph = [[MAX]*n for _ in range(n)]
    graph[startX][startY] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([[startX, startY]])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nr, nc = x, y
            while True:
                nr = nr +dx[i]
                nc = nc +dy[i]
                if nr<0 or nr>=n or nc<0 or nc>=n:
                    break

                if grid[nr][nc] == 'X':
                    break

                if graph[nr][nc] > graph[x][y]+1 :
                    graph[nr][nc] = graph[x][y]+1
                    queue.append((nr,nc))

    return graph[goalX][goalY]

if __name__ == '__main__':
    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()
    startX = int(first_multiple_input[0])
    startY = int(first_multiple_input[1])
    goalX = int(first_multiple_input[2])
    goalY = int(first_multiple_input[3])
    result = minimumMoves(grid, startX, startY, goalX, goalY)
    print (result)