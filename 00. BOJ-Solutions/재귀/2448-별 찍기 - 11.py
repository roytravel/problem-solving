import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def star(r, c, N):
    if N == 3:
        graph[r][c] = "*"
        graph[r+1][c-1] = "*"
        graph[r+1][c+1] = "*"
        for i in range(-2, 3):
            graph[r+2][c+i] = "*"
    else:
        n = N // 2
        star(r, c, n)
        star(r+n, c-n, n)
        star(r+n, c+n, n)

N = int(input())
graph = [[' ']*(N*2) for _ in range(N)]
star(0, N-1, N)
for row in graph:
    print ("".join(row))