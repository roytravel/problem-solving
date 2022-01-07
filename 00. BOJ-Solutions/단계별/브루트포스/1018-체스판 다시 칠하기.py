N, M = list(map(int, input().split()))
chessboard = []
counts = []

for i in range(N):
    value = input()
    if len(value) != M:
        raise ValueError('You must size of chessboard that you input')
    chessboard.append(value)
#print (chessboard)

for x in range(0, N - 8 + 1): # Abstract
    for y in range(0, M - 8 + 1): # Abstract
        white_start, black_start = 0, 0
        for i in range(x, x + 8): # Concrete
            for j in range(y, y + 8): # Concrete
                if (i + j) % 2 == 0:
                    if chessboard[i][j] != "W":
                        white_start +=1
                    if chessboard[i][j] != "B":
                        black_start +=1

                elif (i + j) % 2 == 1:
                    if chessboard[i][j] != "B":
                        white_start +=1
                    if chessboard[i][j] != "W":
                        black_start +=1
        counts.append(white_start)
        counts.append(black_start)

print (min(counts))