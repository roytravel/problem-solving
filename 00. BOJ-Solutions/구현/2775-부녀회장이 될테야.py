import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a = int(input())
    b = int(input())

    apart = [[0 for _ in range(15)] for _ in range(15)]
    for i in range(1, 15):
        apart[0][i] = i
    
    for i in range(1, 15):
        for j in range(1, 15):
            apart[i][j] = sum(apart[i-1][:j+1])

    print (apart[a][b])