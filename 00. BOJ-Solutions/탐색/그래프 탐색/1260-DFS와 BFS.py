import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = dict()
visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)


def dfs(start, graph):
    print (start, end = ' ')
    visited_dfs[start] = True
    for i in graph[start]:
        if not visited_dfs[i]:
            dfs(i, graph)
            visited_dfs[i] = True


def bfs(start, graph):
    queue = deque([start])
    visited_bfs[start] = True
    while queue:
        node = queue.popleft()
        print (node, end = ' ')
        for i in graph[node]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)


for i in range(N):
    graph[i+1] = set()

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)


for key, value in graph.items():
    graph[key] = sorted(value)

dfs(V, graph)
print()
bfs(V, graph)