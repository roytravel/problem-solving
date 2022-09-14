import sys
#sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y, z):
    global answer
    # Check if the pape has all the same number
    visited = graph[x][y]
    for i in range(x, x+z):
        for j in range(y, y+z):
            # What if it doesn't, split it by 9.
            if graph[i][j] != visited:
                for k in range(3):
                    for l in range(3):
                        dfs(x+k*z//3, y+l*z//3, z//3)
                return

    if visited == -1:
        answer[0] += 1
    elif visited == 0:
        answer[1] += 1
    elif visited == 1:
        answer[2] += 1

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0, 0]
dfs(0, 0, N)
for i in answer:
    print (i)