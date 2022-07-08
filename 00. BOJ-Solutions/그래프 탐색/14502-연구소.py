import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
lab = []

def make_wall(count):
    if count == 3:
        spread_virus()
        return

    for x in range(N):
        for y in range(M):
            if lab[x][y] == 0:
                lab[x][y] = 1
                make_wall(count+1)
                lab[x][y] = 0

def spread_virus():
    graph = deepcopy(lab)
    queue = deque()
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                queue.append([i, j])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append([nx, ny])
    cnt = 0
    global answer
    for i in range(N):
        cnt += graph[i].count(0)
    
    answer = max(answer, cnt)
    
        
for _ in range(N):
    lab.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
make_wall(0)
print (answer)