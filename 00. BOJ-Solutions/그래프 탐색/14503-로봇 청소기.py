# -*- coding:utf-8 -*-
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
visited = [[0] * M for _ in range(N)]
r, c, d = map(int,input().split())
dx = [-1, 0, 1, 0] # 0: ����, 1: ����, 2: ����, 3: ���� // �ݽð� ����
dy = [0, 1, 0, -1]
graph = [list(map(int,input().split())) for _ in range(N)]
visited[r][c] = True
count = 1

while True:
    flag = False
    for _ in range(4):
        nx = r + dx[(d+3)%4] # �ݽð� ���� ���� ������
        ny = c + dy[(d+3)%4]
        d = (d+3)%4 # �ѹ� �������� �� �������� �۾�����
        if 0 <=nx<N and 0<=ny<M and graph[nx][ny] == 0:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                count += 1
                r, c = nx, ny
                flag = True #û�� �� �����̶� ������ �������� �Ѿ
                break

    if not flag: # �� ���� ��� Ŭ�� �� ���
        if graph[r-dx[d]][c-dy[d]] == 1: # ������ ���� ���
            print(count)
            break
        else:
            r, c = r-dx[d], c-dy[d]
