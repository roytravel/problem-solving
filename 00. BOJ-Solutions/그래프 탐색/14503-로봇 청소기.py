# -*- coding:utf-8 -*-
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
visited = [[0] * M for _ in range(N)]
r, c, d = map(int,input().split())
dx = [-1, 0, 1, 0] # 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽 // 반시계 방향
dy = [0, 1, 0, -1]
graph = [list(map(int,input().split())) for _ in range(N)]
visited[r][c] = True
count = 1

while True:
    flag = False
    for _ in range(4):
        nx = r + dx[(d+3)%4] # 반시계 방향 순서 생성식
        ny = c + dy[(d+3)%4]
        d = (d+3)%4 # 한번 돌았으면 그 방향으로 작업시작
        if 0 <=nx<N and 0<=ny<M and graph[nx][ny] == 0:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                count += 1
                r, c = nx, ny
                flag = True #청소 한 방향이라도 했으면 다음으로 넘어감
                break

    if not flag: # 네 방향 모두 클린 할 경우
        if graph[r-dx[d]][c-dy[d]] == 1: # 후진시 벽일 경우
            print(count)
            break
        else:
            r, c = r-dx[d], c-dy[d]
