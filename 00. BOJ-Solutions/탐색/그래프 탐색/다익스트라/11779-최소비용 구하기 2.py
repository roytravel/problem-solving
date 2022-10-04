import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    nearest = [start] * (N+1)
    distance = [1e9] * (N+1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        cost, now = heapq.heappop(heap)
        if cost > distance[now]:
            continue
        for n, c in graph[now]:
            C = cost + c
            if distance[n] > C:
                distance[n], nearest[n] = C, now
                heapq.heappush(heap, (C, n))
    return distance, nearest

N = int(input()) # city (vertex)
M = int(input()) # bus (edge)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    src, dst, cost = map(int, input().split())
    graph[src].append([dst, cost])

start, end = map(int, input().split())
distance, nearest = dijkstra(start)

path = [end]
now = end
while now != start:
    now = nearest[now]
    path.append(now)
path.reverse()

print (distance[end])
print(len(path))
print (" ".join(map(str, path)))