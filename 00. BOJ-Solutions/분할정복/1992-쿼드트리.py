import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def quad_tree(x, y, N):
    global answer
    color = graph[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != graph[i][j]:
                answer += "("
                quad_tree(x, y, N//2)
                quad_tree(x, y+N//2, N//2)
                quad_tree(x+N//2, y, N//2)
                quad_tree(x+N//2, y+N//2, N//2)
                answer += ")"
                return
    answer.append(color)

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
answer = []
quad_tree(0, 0, N)
print ("".join(map(str, answer)))