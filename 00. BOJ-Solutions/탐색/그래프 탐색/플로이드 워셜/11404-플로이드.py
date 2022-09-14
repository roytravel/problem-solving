import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = float('inf')
graph = [[INF] * n for _ in range(n)]

for _ in range(m):
    src, dst, cost = map(int, input().split())
    graph[src-1][dst-1] = min(graph[src-1][dst-1], cost)

for k in range(n): # via
    graph[k][k] = 0
    for i in range(n): # src
        for j in range(n): # dst
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in graph:
    for j in i:
        if j == INF:
            print (0, end = ' ')
        else:
            print (j, end = ' ')
    print()