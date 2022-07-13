# -*- coding:utf-8 -*-
import sys
input = sys.stdin.readline

N = int(input())
students = []
array = []
students = [list(map(int, input().split())) for _ in range(N*N)]
array = [[0] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N*N):
    student = students[i]
    temp = []
    for x in range(N):
        for y in range(N):
            if array[x][y] == 0:
                like = 0
                blank = 0
                for _ in range(4):
                    nx = x + dx[_]
                    ny = y + dy[_]
                    if 0 <= nx < N and 0 <= ny < N:
                        if array[nx][ny] in student[1:]: # 좋아하는 학생이 인접할 경우
                            like += 1
                        if array[nx][ny] == 0: # 공백일 경우
                            blank += 1

                temp.append([like, blank, x, y])
    temp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3])) # 좋음/공백은 내림차순, 행/열은 오름차순
    array[temp[0][2]][temp[0][3]] = student[0]

students.sort()
answer = 0
result = 0
for x in range(N):
    for y in range(N):
        answer = 0
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]

            if 0<=nx<N and 0<=ny<N:
                if array[nx][ny] in students[array[x][y]-1]:
                    answer += 1
        if answer != 0:
            result += 10 ** (answer-1)
            
print(result)