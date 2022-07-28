# -*- coding:utf-8 -*-
import sys
input = sys.stdin.readline

def check(array):
    n = len(array)
    answer = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if array[i][j] == array[i][j-1]: # �� ��ȸ: ���� ���� ����
                cnt += 1 
            else:
                cnt=1
            if cnt > answer: # ���� cnt�� �� ũ�� answer ����
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
        if j+1 < n: # �� ����
            array[i][j], array[i][j+1] = array[i][j+1], array[i][j] # ������ ĵ�� ����
            temp = check(array) # �������� �� ���� �� ������ �κ�
            if temp > answer:
                answer = temp
            array[i][j], array[i][j+1] = array[i][j+1], array[i][j] # ���� ����
            
        if i+1 < n: # �� ����
            array[i][j], array[i+1][j] = array[i+1][j], array[i][j]
            temp = check(array)
            if temp > answer:
                answer = temp
            array[i][j], array[i+1][j] = array[i+1][j], array[i][j]
print(answer)