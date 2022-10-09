import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    heap = []
    distances = [float('inf')] * (D+1)
    distances[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        cost, now = heapq.heappop(heap)
        if cost > distances[now]:
            continue
        
        for n, c in graph[now]:
            C = cost + c
            if distances[n] > C:
                distances[n] = C
                heapq.heappush(heap, (C, n))
    return distances[D]

N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]

for i in range(D):
    graph[i].append([i+1, 1]) # why this operation is performed? because this operation means a car running on a highway

for _ in range(N):
    src, dst, cost = map(int, input().split())
    if dst > D:
        continue
    graph[src].append([dst, cost])

print (dijkstra(0))