# # Solution 1: BFS
# import sys
# from collections import defaultdict, deque
# input = sys.stdin.readline

# def bfs(start):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         x = queue.popleft()
#         for node in graph[x]:
#             if not visited[node]:
#                 visited[node] = visited[x] + 1
#                 queue.append(node)

# N, M = map(int, input().split())
# graph = defaultdict(list)
# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# answer = []
# for i in range(1, N+1):
#     visited = [False] * (N+1)
#     bfs(i)
#     answer.append(sum(visited))

# print (answer.index(min(answer))+1)


# Solution 2: Floyd-Warshall
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

INF = float('INF')
graph = [[INF] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for k in range(N): # via
    graph[k][k] = 0
    for i in range(N): # src
        for j in range(N): # dst
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
for i in range(N):
    temp = sum(graph[i])
    if INF > temp:
        INF = temp
        answer = i

print (answer+1)