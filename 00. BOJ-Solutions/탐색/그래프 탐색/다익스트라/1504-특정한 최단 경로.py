import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    heap = []
    distance = [INF] * (V+1)
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        cost, now = heapq.heappop(heap)
        if cost > distance[now]:
            continue
        
        for n, c in graph[now]:
            C = cost + c 
            if distance[n] > C:
                distance[n] = C
                heapq.heappush(heap, (C, n))
    return distance

V, E = map(int, input().split())
INF = float('inf')
graph = [[] for _ in range(V+1)]

for _ in range(E):
    src, dst, cost = map(int, input().split())
    graph[src].append([dst, cost]) # because there is no direction
    graph[dst].append([src, cost]) # because there is no direction

v1, v2 = map(int, input().split())

distance1 = dijkstra(1)
distance2 = dijkstra(v1)
distance3 = dijkstra(v2)

path1 = distance1[v1] + distance2[v2] + distance3[V]
path2 = distance1[v2] + distance3[v1] + distance2[V]
result = min(path1, path2)
print (result if result < INF else -1)