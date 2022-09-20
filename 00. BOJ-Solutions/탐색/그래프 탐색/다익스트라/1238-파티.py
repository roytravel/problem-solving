import sys
import heapq

def dijkstra(src):
    heap = []
    INF = float('inf')
    costs = [INF] * (V+1)
    heapq.heappush(heap, (0, src))
    costs[src] = 0

    while heap:
        cost, num = heapq.heappop(heap)
        if cost > costs[num]:
            continue

        for d, c in graph[num]:
            C = cost + c
            if costs[d] > C:
                costs[d] = C
                heapq.heappush(heap, (C, d))
    return costs 

input = sys.stdin.readline
V, E, X = map(int, input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    src, dst, cost = map(int, input().split())
    graph[src].append([dst, cost])

answer = 0
for i in range(1, V+1):
    go = dijkstra(i)
    back = dijkstra(X)
    answer = max(answer, go[X] + back[i])

print (answer)