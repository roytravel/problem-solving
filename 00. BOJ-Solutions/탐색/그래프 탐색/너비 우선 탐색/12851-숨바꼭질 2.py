import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    count = 0
    queue = deque([start])
    visited[start] = 1
    while queue:
        x = queue.popleft()
        if x == K:
            count += 1
        for nx in [x-1, x+1, x*2]:
            if 0<=nx<100001:
                if not visited[nx] or visited[nx] >= visited[x]+1: # I don't get it why post condition is required?
                    visited[nx] = visited[x]+1
                    queue.append(nx)
    return count

N, K = map(int, input().split())
visited = [0] * (100_001)
count = bfs(N)
print(visited[K]-1) # because it was started from 1.
print(count)