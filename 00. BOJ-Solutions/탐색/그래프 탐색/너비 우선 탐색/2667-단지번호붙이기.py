import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
building = []

def post_house_name():
    queue = deque()
    counts = []
    for i in range(N):
        for j in range(N):
            if building[i][j] == 1:
                queue.append([i, j])
                count = 1
                while queue:
                    x, y = queue.popleft()
                    building[x][y] = 0
                    for _ in range(4):
                        nx = x + dx[_]
                        ny = y + dy[_]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue
                        if building[nx][ny] == 1:
                            building[nx][ny] = 0
                            queue.append([nx, ny])
                            count += 1
                counts.append(count)

    counts.sort()
    print (len(counts))
    for i in counts:
        print (i)

for _ in range(N):
    building.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
# post_house_name()

# DFS 
def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    
    if building[x][y] == 1:
        global count
        count += 1

        building[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

count = 0
counts = []
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            counts.append(count)
            count = 0

counts.sort()
print (len(counts))
for i in counts:
    print (i)