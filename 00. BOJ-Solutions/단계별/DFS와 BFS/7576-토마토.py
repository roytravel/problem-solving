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

    # �ʱ� ���� ���� & �׷��� ����
    M, N = list(map(int, input().split()))
    graph = []
    queue = deque()

    dx = [-1, 0, 1, 0] # ���� �丶�� ��ǥ �������� ����� ������� ���� x��ǥ
    dy = [0, -1, 0, 1] # ���� �丶�� ��ǥ �������� ����� ������� ���� y��ǥ

    for i in range(N):
        graph.append(list(map(int,input().split())))

    # ���� �丶�� ��ǥ ���� -> ť ����

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append([i, j])
    
    # �丶�� ����
    graph = bfs()

    # ��� ���
    day = 0
    for i in graph:
        for j in i:
            if j == 0:
                print (-1)
                exit(0)
        day = max(day, max(i))
    
    print (day-1)