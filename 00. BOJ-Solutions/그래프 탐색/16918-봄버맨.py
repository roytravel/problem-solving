import sys
from collections import deque
input = sys.stdin.readline

def bfs(initial):
    queue = deque(initial)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<R and 0<=ny<C:
                grid[nx][ny] = "."
                grid[x][y] = "."

def get_bomb_coordinates():        
    for i in range(R):
        for j in range(C):
            if grid[i][j] == "O":
                initial.append([i, j])


def install_all_bombs():
    for i in range(R):
        for j in range(C):
            if grid[i][j] == ".":
                grid[i][j] = "O"

def explod(initial):
    while initial:
        x, y = initial.popleft()
        grid[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<R and 0<=ny<C:
                grid[nx][ny] = '.'

R, C, N = map(int, input().split())
grid = []
for _ in range(R):
    grid.append(list(input().strip()))
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

N = N-1
while N:
    initial = deque()
    get_bomb_coordinates() # get inital coordinates of bomb
    install_all_bombs() # install bombs in all seats
    N = N - 1
    if N == 0:
        break
    explod(initial)
    N = N - 1

for i in range(len(grid)):
    for j in range(len(grid[0])):
        print (grid[i][j], end='')
    print()