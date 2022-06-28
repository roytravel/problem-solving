import sys
from collections import deque
input = sys.stdin.readline

computer = int(input())
pair = int(input())
graph = dict()
visited = []

# def dfs(start, graph):
#     for i in graph[start]:
#         if i not in visited:
#             visited.append(i)
#             dfs(i, graph)

def bfs(start, graph):
    queue = deque([start])
    while queue:
        for i in graph[queue.popleft()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
            
for i in range(computer):
    graph[i+1] = set()

for j in range(pair):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

bfs(1, graph)
#dfs(1, graph)
print (len(visited)-1)