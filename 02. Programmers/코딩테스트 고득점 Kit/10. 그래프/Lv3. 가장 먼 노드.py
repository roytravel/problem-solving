from collections import deque

def solution(n, edge):
    graph =[[] for _ in range(n+1)]
    dist = [0 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    visited[1] = True
    queue = deque([1])
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                dist[i] = dist[x] + 1

    dist.sort(reverse=True)
    answer = dist.count(dist[0])
    return answer

# from collections import deque

# def solution(n, edge):
#     visited = [False for _ in range(n+1)]
#     graph = [[] for _ in range(n+1)]
#     for u, v in edge:
#         graph[u].append(v)
#         graph[v].append(u)
    
#     visited[1] = True
    
#     queue = deque([1])
#     while queue:
#         x = queue.popleft()
#         for i in graph[x]:
#             if visited[i] == False:
#                 visited[i] = visited[x] + 1
#                 queue.append(i)
#     MAX = max(visited)
#     count = visited.count(MAX)
        
#     return count if count > 0 else 1

print (solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))