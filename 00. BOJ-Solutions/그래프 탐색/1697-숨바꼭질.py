import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
MAX = 10**5
visited = [0] * (MAX + 1)
""" 
5 17
5 -> 10 -> 9 -> 18 -> 17
"""

def bfs(start):
    queue = deque([start])
    while queue:
        x = queue.popleft()
        if x == K:
            print (visited[x])
            break
        for i in (x+1, x-1, x*2):
            if 0 <= i <= MAX and not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)
bfs(N)