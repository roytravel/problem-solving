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
#                 queue.append([a, b, c]) # �湮���� ���� ���� ��带 ť�� ����
#                 graph[a][b][c] = graph[x][y][z] + 1
#                 print (queue)

#     return graph

# if __name__ == "__main__":

#     # �ʱ� ���� ���� & �׷��� ����
#     M, N, H = list(map(int, input().split()))
#     graph = [[[0 for i in range(M)] for j in range(N)] for k in range(H)]
#     queue = deque()

#     dx = [0, 0, 0, 1, 1, 1] # ���� �丶�� ��ǥ �������� ����� ������� ���� x��ǥ
#     dy = [0, 1, 1, 0, 0, 1] # ���� �丶�� ��ǥ �������� ����� ������� ���� y��ǥ
#     dz = [1, 0, 1, 0, 1, 0]

#     for i in range(H):
#         for j in range(N):
#             graph[i][j] = list(map(int, sys.stdin.readline().split()))

#     print (graph)
    
    
#     # ���� �丶�� ��ǥ ���� -> ť ����
#     for i in range(H):
#         for j in range(N):
#             for k in range(M):
#                 if graph[i][j][k] == 1:
#                     queue.append([i, j, k])
    
#     print (queue)
#     # �丶�� ����
#     graph = bfs()

#     # ��� ���
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
m,n,h = map(int,input().split()) # mnũ��, h���ڼ�
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