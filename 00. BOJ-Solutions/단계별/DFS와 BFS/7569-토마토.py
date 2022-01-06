# # -*- coding:utf-8 -*-
# import sys
# from collections import deque

# def bfs() -> list:
#     while queue:
#         x, y, z = queue.popleft()
#         for i in range(6):
#             a = x + dx[i]
#             b = y + dy[i]
#             c = z + dz[i]
#             if 0<=a<H and 0<=b<N and 0<=c<M and graph[a][b][c] == 0:
#                 queue.append([a, b, c]) # 방문하지 않은 다음 노드를 큐에 삽입
#                 graph[a][b][c] = graph[x][y][z] + 1
#                 print (queue)

#     return graph

# if __name__ == "__main__":

#     # 초기 변수 선언 & 그래프 생성
#     M, N, H = list(map(int, input().split()))
#     graph = [[[0 for i in range(M)] for j in range(N)] for k in range(H)]
#     queue = deque()

#     dx = [0, 0, 0, 1, 1, 1] # 익은 토마토 좌표 기준으로 사방향 드로잉을 위한 x좌표
#     dy = [0, 1, 1, 0, 0, 1] # 익은 토마토 좌표 기준으로 사방향 드로잉을 위한 y좌표
#     dz = [1, 0, 1, 0, 1, 0]

#     for i in range(H):
#         for j in range(N):
#             graph[i][j] = list(map(int, sys.stdin.readline().split()))

#     print (graph)
    
    
#     # 익은 토마토 좌표 추출 -> 큐 삽입
#     for i in range(H):
#         for j in range(N):
#             for k in range(M):
#                 if graph[i][j][k] == 1:
#                     queue.append([i, j, k])
    
#     print (queue)
#     # 토마토 숙성
#     graph = bfs()

#     # 결과 출력
#     day = 0
#     print (graph)
#     for i in graph:
#         for j in i:
#             for k in j:
#                 if k == 0:
#                     print (-1)
#                     exit(0)
#             day = max(day, max(i))
#     print (day-1)

import sys
from collections import deque
m,n,h = map(int,input().split()) # mn크기, h상자수
graph = []
queue = deque([])
 
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k]==1:
                queue.append([i,j,k])
    graph.append(tmp)
    
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
while(queue):
    x,y,z = queue.popleft()
    
    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]
        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0:
            queue.append([a,b,c])
            graph[a][b][c] = graph[x][y][z]+1
            
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)