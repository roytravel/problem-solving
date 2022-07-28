import sys
input = sys.stdin.readline
board, order = [], []
for i in range(5):
    board.append(list(map(int, input().split())))
for i in range(5):
    order.append(list(map(int, input().split())))

def checker():
    bingo = 0
    for i in range(5): # row
        if board[i].count(0) == 5:
            bingo += 1
        if bingo == 3: 
            return bingo

    for i in range(5): # col
        flag = True
        for j in range(5):
            if board[j][i] != 0:
                flag = False
        if flag:
            bingo += 1
        if bingo == 3: 
            return bingo

    flag = True # diagonal (left)
    for i in range(5): 
        if board[i][i] != 0:
            flag = False
    if flag:
        bingo += 1

    if bingo == 3:
        return bingo
    
    flag = True # diagonal (right)
    if board[0][4] != 0: flag = False
    if board[1][3] != 0: flag = False
    if board[2][2] != 0: flag = False
    if board[3][1] != 0: flag = False
    if board[4][0] != 0: flag = False

    if flag:
        bingo += 1
    
    if bingo == 3:
        return bingo
    
    return bingo

count = 0
stop = False
for i in range(5):
    if stop: 
        break
    for j in range(5):
        count += 1
        value = order[i][j]
        stop2 = False
        for k in range(5):
            if stop2:
                break
            for l in range(5):
                if value == board[k][l]:
                    board[k][l] = 0
                    stop2 = True
                    break
        bingo = checker()
        if bingo == 3:
            print(count)
            stop = True
            break