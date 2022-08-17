# coding:utf-8

from collections import defaultdict

def solution(n, results):
    answer = 0
    winer = defaultdict(set)
    loser = defaultdict(set)
    
    for win, lose in results: # ��� �׷���ȭ
        winer[lose].add(win)
        loser[win].add(lose)

    for i in range(1, n+1):
        for win in winer[i]: # i���� �¸��� ����̸� i���� �й��� ������Ե� �¸��� ��
            loser[win].update(loser[i])
        for lose in loser[i]: # i���� �й��� ����̸� i���� �¸��� ������Ե� �й��� ��
            winer[lose].update(winer[i])
    
    for i in range(1, n+1):
        if len(winer[i]) + len(loser[i]) == n-1: # i���� �̱�� �� ��� ���� n-1�̸� ���� ����
            answer += 1
    return answer

# def solution(n, results):
#     answer = 0
#     graph = [[int(1e9)] * (n+1) for _ in range(n+1)]
#     for i, j in results:
#         graph[i][j] = 1
    
#     for i in range(1, n+1): # �ڱ� �ڽ����� ���� ��� 0 (����Ŭ ���� ���)
#         for j in range(1, n+1):
#             if i == j:
#                 graph[i][j] = 0

#     for k in range(1, n+1): # �ش� ���� ���ų� �� �� ������ �����񱳰� ����
#         for i in range(1, n+1):
#             for j in range(1, n+1):
#                 graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

#     count = 0
#     for i in range(1, n+1):
#         count = 0
#         for j in range(1, n+1):            
#             if graph[i][j] != int(1e9) or graph[j][i] != int(1e9): #�ش� ���� ���ų� �� �� ������ ������ ����
#                 count += 1
#         if count == n:
#             answer += 1

#     return answer

# def solution(n, results):
#     answer = 0
#     winer = [[] for _ in range(n+1)]
#     lose = [[] for _ in range(n+1)]

#     for win, lose in results:
#         winer[win].append(lose)
#         lose[lose].append(win)

#     for i in range(1, n+1):
#         for win in winer[i]:
#             if lose[i]:
#                 for lose in lose[i]:
#                     if lose not in lose[win]:
#                         lose[win].append(lose)
#                     if win not in winer[lose]:
#                         winer[lose].append(win)

#     for win, lose in zip(winer, lose):
#         if len(win) + len(lose) == n-1:
#             answer+=1
#     return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))