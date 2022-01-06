# -*- coding:utf-8 -*-
from collections import deque

def bfs() -> list:
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]

            if 0<=a<N and 0<=b<M and graph[a][b] == 0:
                queue.append([a, b])
                graph[a][b] = graph[x][y] + 1

    return graph

if __name__ == "__main__":

    # 초기 변수 선언 & 그래프 생성
    M, N = list(map(int, input().split()))
    graph = []
    queue = deque()

    dx = [-1, 0, 1, 0] # 익은 토마토 좌표 기준으로 사방향 드로잉을 위한 x좌표
    dy = [0, -1, 0, 1] # 익은 토마토 좌표 기준으로 사방향 드로잉을 위한 y좌표

    for i in range(N):
        graph.append(list(map(int,input().split())))

    # 익은 토마토 좌표 추출 -> 큐 삽입

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append([i, j])
    
    # 토마토 숙성
    graph = bfs()

    # 결과 출력
    day = 0
    for i in graph:
        for j in i:
            if j == 0:
                print (-1)
                exit(0)
        day = max(day, max(i))
    
    print (day-1)