import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(start, depth):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth+1)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        if not graph[i]:
            count +=1
            visited[i] = True
        else:
            dfs(i, 0)
            count += 1
print (count)