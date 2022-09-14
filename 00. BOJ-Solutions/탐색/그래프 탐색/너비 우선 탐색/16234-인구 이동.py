""" Refer: https://resilient-923.tistory.com/353"""
import sys
input = sys.stdin.readline
from collections import deque

country = []
N, L, R = map(int,input().split())
for _ in range(N):
    country.append(list(map(int,input().split())))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def move_country(a,b):
    queue = deque()
    temp = []
    queue.append([a, b])
    temp.append([a, b])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                if L<=abs(country[nx][ny] - country[x][y]) <=R:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                    temp.append([nx, ny])
    return temp
            
count = 0
while True:
    visited = [[0] * (N+1) for _ in range(N+1)]
    flag = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                temp = move_country(i,j)

                if len(temp) > 1:
                    flag = True
                    people = 0
                    for x, y in temp:
                        people += country[x][y]
                        avg_people = people // len(temp)
                    for x,y in temp:
                        country[x][y] = avg_people
    # 연합 해제 
    if flag == 0:
        break

    count += 1
print(count)