import sys
input  = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(start):
    for i in graph[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i)

N = int(input())
graph = [[] for _ in range(N+1)]
parents = [0 for _ in range(N+1)]

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


dfs(1)

for i in range(2, N+1):
    print (parents[i])