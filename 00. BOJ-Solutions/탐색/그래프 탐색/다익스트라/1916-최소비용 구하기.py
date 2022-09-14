import sys
import heapq
input = sys.stdin.readline

def dijkstra(x):
    visited[x] = 0
    heap = []
    heapq.heappush(heap, (0, x))
    while heap:
        weight, num = heapq.heappop(heap)
        if weight > visited[num]:
            continue

        for n, w in graph[num]:
            W = weight + w
            if visited[n] > W:
                visited[n] = W
                heapq.heappush(heap, (W, n))

N = int(input())
M = int(input())
INF = float('inf')
graph = [[] for _ in range(N+1)]
visited = [INF for _ in range(N+1)]

for i in range(M):
    A, B, W = map(int, input().split())
    graph[A].append([B, W])

start, end = map(int, input().split())
dijkstra(start)
print (visited[end])