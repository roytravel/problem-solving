# DFS
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x, w):
    for node, weight in graph[x]:
        if dist[node] == -1:
            dist[node] = weight + w
            dfs(node, weight+w)

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append([child, weight])
    graph[child].append([parent, weight])

dist = [-1] * (N+1)
dist[1] = 0
dfs(1, 0)

node = dist.index(max(dist))
dist = [-1] * (N+1)
dist[node] = 0
dfs(node, 0)
print(max(dist))

# BFS (It doesn't work)
# import sys
# from collections import deque
# input = sys.stdin.readline

# def bfs(start, num):
#     queue = deque([start, 0])
#     visited = [-1] * (n+1)
#     visited[start] = 0
#     while queue:
#         x = queue.popleft()
#         for node, weight in graph[x]:
#             if visited[node] == -1:
#                 visited[node] = visited[x] + weight
#                 queue.append(node)
#     if num == 1:
#         return visited.index(max(visited))
#     else:
#         return max(visited)

# n = int(input())
# graph = [[] for _ in range(n+1)]
# for _ in range(n-1):
#     parent, child, weight = map(int, input().split())
#     graph[parent].append([child, weight])
#     graph[child].append([parent, weight])

# print (bfs(bfs(0, 1), 2))