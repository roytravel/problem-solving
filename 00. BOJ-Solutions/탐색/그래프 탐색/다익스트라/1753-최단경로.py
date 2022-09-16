import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    dp[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        weight, num = heapq.heappop(heap)
        if weight > dp[num]:
            continue 

        for n, w in graph[num]:
            W = weight + w
            if dp[n] > W:
                dp[n] = W
                heapq.heappush(heap, (W, n))

INF = float('inf')
V, E = map(int, input().split())
dp = [INF] * (V+1)
graph = [[] for _ in range(V+1)]

start = int(input())
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

dijkstra(start)
for i in range(1, V+1):
    if dp[i] == INF:
        print ("INF")
    else:
        print (dp[i])