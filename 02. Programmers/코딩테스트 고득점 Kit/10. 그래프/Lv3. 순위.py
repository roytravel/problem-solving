# coding:utf-8

from collections import defaultdict

def solution(n, results):
    answer = 0
    winer = defaultdict(set)
    loser = defaultdict(set)
    
    for win, lose in results: # 결과 그래프화
        winer[lose].add(win)
        loser[win].add(lose)

    for i in range(1, n+1):
        for win in winer[i]: # i에게 승리한 사람이면 i에게 패배한 사람에게도 승리한 것
            loser[win].update(loser[i])
        for lose in loser[i]: # i에게 패배한 사람이면 i에게 승리한 사람에게도 패배한 것
            winer[lose].update(winer[i])
    
    for i in range(1, n+1):
        if len(winer[i]) + len(loser[i]) == n-1: # i에게 이기고 진 사람 합해 n-1이면 순위 결정
            answer += 1
    return answer

# def solution(n, results):
#     answer = 0
#     graph = [[int(1e9)] * (n+1) for _ in range(n+1)]
#     for i, j in results:
#         graph[i][j] = 1
    
#     for i in range(1, n+1): # 자기 자신으로 가는 경우 0 (사이클 생길 경우)
#         for j in range(1, n+1):
#             if i == j:
#                 graph[i][j] = 0

#     for k in range(1, n+1): # 해당 노드로 오거나 갈 수 있으면 순위비교가 가능
#         for i in range(1, n+1):
#             for j in range(1, n+1):
#                 graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

#     count = 0
#     for i in range(1, n+1):
#         count = 0
#         for j in range(1, n+1):            
#             if graph[i][j] != int(1e9) or graph[j][i] != int(1e9): #해당 노드로 오거나 갈 수 있으면 순위비교 가능
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