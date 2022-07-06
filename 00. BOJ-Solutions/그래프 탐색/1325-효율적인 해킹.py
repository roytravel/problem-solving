import sys
import collections
input = sys.stdin.readline

def bfs(start):
    count = 1
    visited = [False] * (N+1)
    visited[start] = True
    queue = collections.deque([start])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                count += 1
    return count

N, M = map(int, input().split())
graph = collections.defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

result = []
max_count = 1
for i in range(1, N+1):
    count = bfs(i) # 4, 4, 3, 1, 1
    if count > max_count:
        max_count = count
        result.clear()
        result.append(i)
    elif count == max_count:
        result.append(i)
        
print(*result)