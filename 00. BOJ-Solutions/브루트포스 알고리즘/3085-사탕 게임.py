# -*- coding:utf-8 -*-
import sys
input = sys.stdin.readline

def check(array):
    n = len(array)
    answer = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if array[i][j] == array[i][j-1]: # 열 순회: 연속 숫자 세기
                cnt += 1 
            else:
                cnt=1
            if cnt > answer: # 현재 cnt가 더 크면 answer 갱신
                answer = cnt
        cnt = 1
        for j in range(1, n):
            if array[j][i] == array[j-1][i]:
                cnt += 1
            else:
                cnt=1
            if cnt > answer:
                answer = cnt
    return answer

n = int(input())
array = [list(input()) for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        if j+1 < n: # 열 변경
            array[i][j], array[i][j+1] = array[i][j+1], array[i][j] # 인접한 캔디 변경
            temp = check(array) # 변경했을 때 가장 긴 연속한 부분
            if temp > answer:
                answer = temp
            array[i][j], array[i][j+1] = array[i][j+1], array[i][j] # 변경 복귀
            
        if i+1 < n: # 행 변경
            array[i][j], array[i+1][j] = array[i+1][j], array[i][j]
            temp = check(array)
            if temp > answer:
                answer = temp
            array[i][j], array[i+1][j] = array[i+1][j], array[i][j]
print(answer)