import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance = [float('inf') for _ in range(N+1)]
    distance[start] = 0
    while heap:
        cost, now = heapq.heappop(heap)
        if cost > distance[now]:
            continue

        for n, c in graph[now]:
            C = cost + c
            if C > M:
                continue
            if distance[n] > C:
                distance[n] = C
                heapq.heappush(heap, (C, n))

    return distance

N, M, R = map(int, input().split())
items = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

for _ in range(R):
    src, dst, cost = map(int, input().split())
    graph[src].append([dst, cost])
    graph[dst].append([src, cost])

answer = []
for i in range(1, len(items)+1):
    distance = dijkstra(i)
    s = 0
    for j in range(len(distance)):
        if distance[j] != float('inf'):
            s += items[j-1]
    answer.append(s)
print (max(answer))