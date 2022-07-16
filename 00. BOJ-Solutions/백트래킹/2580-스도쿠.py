import sys
input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(9)]
blank = []

for i in range(9):
    for j in range(9):
        if not board[i][j]:
            blank.append([i, j])

def check_row(x, num):
    for i in range(9):
        if num == board[x][i]:
            return False
    return True

def check_col(y, num):
    for i in range(9):
        if num == board[i][y]:
            return False
    return True

def check_rect(x, y, num):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if num == board[nx+i][ny+j]:
                return False
    return True

def dfs(index):
    if index == len(blank):
        for i in range(9):
            print (*board[i])
        exit(0)

    for num in range(1, 10):
        x = blank[index][0]
        y = blank[index][1]
        if check_row(x, num) and check_col(y, num) and check_rect(x, y, num):
            board[x][y] = num
            dfs(index+1)
            board[x][y] = 0

dfs(0)