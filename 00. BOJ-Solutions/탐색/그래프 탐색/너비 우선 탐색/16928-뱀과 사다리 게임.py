import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    while queue:
        x = queue.popleft()
        if x == 100:
            print (graph[x])
            break
    
        for i in range(1, 7):
            dice = x + i
            if dice <= 100 and not visited[dice]:
                if dice in up.keys():
                    dice = up[dice]
                
                if dice in down.keys():
                    dice = down[dice]
                
                if not visited[dice]:
                    visited[dice] = True
                    graph[dice] = graph[x] + 1
                    queue.append(dice)

N, M = map(int, input().split())
dice = 0
up, down = dict(), dict()
graph = [0] * 101
visited = [False] * 101

for _ in range(N):
    x, y = map(int, input().split())
    up[x] = y

for _ in range(M):
    x, y = map(int, input().split())
    down[x] = y

bfs(1)