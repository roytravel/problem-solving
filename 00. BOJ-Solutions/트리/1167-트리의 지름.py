import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visited = [-1] * (V+1)
    queue = deque([start])
    visited[start] = 0
    answer = [0, 0]
    while queue:
        x = queue.popleft()
        for edge, weight in graph[x]:
            if visited[edge] == -1:
                visited[edge] = visited[x] + weight
                queue.append(edge)
                if visited[edge] > answer[0]:
                    answer = visited[edge], edge
    return answer
                
V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    tree = list(map(int, input().split()))
    for i in range(1, len(tree)-2, 2):
        graph[tree[0]].append([tree[i], tree[i+1]])

distance, node = bfs(1)
distance, node = bfs(node)
print (distance)