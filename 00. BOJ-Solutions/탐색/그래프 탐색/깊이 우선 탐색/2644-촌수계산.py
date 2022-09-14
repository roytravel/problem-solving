import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(node):
    for n in graph[node]:
        if check[n] == 0:
            check[n] = check[node] + 1
            print (n, node, graph, check )
            dfs(n)

def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if check[n] == 0:
                check[n] = check[node] + 1
                queue.append(n)

n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
check = [0] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(start)
#bfs(start)
if check[end] > 0:
    print (check[end])
else:
    print (-1)