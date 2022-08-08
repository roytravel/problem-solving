from collections import deque

def bfs(src, visited, graph):
    queue = deque([src])
    visited[src] = True
    result = 1
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == False:
                result +=1
                queue.append(i)
                visited[i] = True
    return result

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]    
    for src, dst in wires:
        graph[src].append(dst)
        graph[dst].append(src)

    for src, dst in wires:
        visited = [False] * (n+1)
        visited[dst] = True
        result = bfs(src, visited, graph)
        if abs(result - (n-result)) < answer:
            answer = abs(result - (n-result))
    return answer