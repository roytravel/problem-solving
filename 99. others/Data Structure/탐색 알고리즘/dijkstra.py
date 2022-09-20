import heapq

def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])
    INF = float('inf')
    weights = [INF] * (vertex+1)
    weights[start] = 0
    
    while heap:
        weight, node = heapq.heappop(heap)
        if weight > weights[node]:
            continue
        
        for n, w in graph[node]:
            W = weight + w
            if weights[n] > W:
                weights[n] = W
                heapq.heappush(heap, (W, n))

    return weights

vertex, edge, start = 5, 6, 1 # 노드 개수, 간선, 시작점
graph = [[] for _ in range(vertex+1)]
graph[1].append([2, 3])
graph[1].append([4, 8])
graph[1].append([5, 9])
graph[2].append([1, 2])
graph[2].append([3, 2])
graph[3].append([2, 2])
graph[3].append([4, 1])
graph[3].append([5, 3])
graph[4].append([1, 8])
graph[4].append([3, 1])
graph[5].append([1, 9])

weights = dijkstra(start)
print (weights)