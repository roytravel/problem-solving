# coding:utf-8
# from collections import defaultdict, deque
# def solution(arrows):
#     answer = 0
#     move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
#     now = (0, 0)
#     visited = defaultdict(int) # visited : 노드 방문 체크
#     visited_dir = defaultdict(int) # visited_dir : 노드 방문 경로 체크 ((A, B)는 A -> B 경로를 의미)
#     queue = deque([now]) # arrows 따라 노드 좌표를 큐에 추가
#     for i in arrows:
#         for _ in range(2): # 모래시계형태 예외처리 위해 진행방향으로 2칸씩 추가
#             next = (now[0]+move[i][0], now[1]+move[i][1])
#             queue.append(next)
#             now = next
#     now = queue.popleft()
#     visited[now] = 1
#     while queue:
#         next = queue.popleft()
#         if visited[next] == 1: # 기 방문 노드인 경우
#             if visited_dir[(now, next)] == 0: # 해당 경로로 처음 들어온 경우인 경우 answer++ 
#                 answer += 1 # 처음 들어온 경우에 방이 처음 생성되므로!
#         else: # 처음 방문한 노드인 경우 방문 체크를 한다.
#             visited[next] = 1
#         visited_dir[(now, next)] = 1 # 해당 노드로 들어온 경로 방문 체크
#         visited_dir[(next, now)] = 1 # 해당 노드로 들어온 경로 방문 체크
#         now = next
#     return answer

from collections import defaultdict
def solution(arrows):
    answer = 0
    visit = defaultdict(list)
    x, y = 0, 0
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    for arrow in arrows:
        for _ in range(2): # 대각선 판별 위해 진행방향으로 2칸씩
            nx = x + dx[arrow]
            ny = y + dy[arrow]
            if (nx, ny) in visit and (x, y) not in visit[(nx, ny)]: # 방문한 점이나 경로가 겹치지 않는 경우 방+1
                answer += 1
                visit[(nx, ny)].append((x, y))
                visit[(x, y)].append((nx, ny))
            elif (nx, ny) not in visit: # 방문하지 않은 경우
                visit[(nx, ny)].append((x, y))
                visit[(x, y)].append((nx, ny)) # 경로 겹치는 경우는 따로 해줄 필요 없음
            x, y = nx, ny # 이동
    return answer

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))