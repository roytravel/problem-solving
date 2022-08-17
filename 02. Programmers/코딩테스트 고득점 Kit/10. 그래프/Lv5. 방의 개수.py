# coding:utf-8
# from collections import defaultdict, deque
# def solution(arrows):
#     answer = 0
#     move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
#     now = (0, 0)
#     visited = defaultdict(int) # visited : ��� �湮 üũ
#     visited_dir = defaultdict(int) # visited_dir : ��� �湮 ��� üũ ((A, B)�� A -> B ��θ� �ǹ�)
#     queue = deque([now]) # arrows ���� ��� ��ǥ�� ť�� �߰�
#     for i in arrows:
#         for _ in range(2): # �𷡽ð����� ����ó�� ���� ����������� 2ĭ�� �߰�
#             next = (now[0]+move[i][0], now[1]+move[i][1])
#             queue.append(next)
#             now = next
#     now = queue.popleft()
#     visited[now] = 1
#     while queue:
#         next = queue.popleft()
#         if visited[next] == 1: # �� �湮 ����� ���
#             if visited_dir[(now, next)] == 0: # �ش� ��η� ó�� ���� ����� ��� answer++ 
#                 answer += 1 # ó�� ���� ��쿡 ���� ó�� �����ǹǷ�!
#         else: # ó�� �湮�� ����� ��� �湮 üũ�� �Ѵ�.
#             visited[next] = 1
#         visited_dir[(now, next)] = 1 # �ش� ���� ���� ��� �湮 üũ
#         visited_dir[(next, now)] = 1 # �ش� ���� ���� ��� �湮 üũ
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
        for _ in range(2): # �밢�� �Ǻ� ���� ����������� 2ĭ��
            nx = x + dx[arrow]
            ny = y + dy[arrow]
            if (nx, ny) in visit and (x, y) not in visit[(nx, ny)]: # �湮�� ���̳� ��ΰ� ��ġ�� �ʴ� ��� ��+1
                answer += 1
                visit[(nx, ny)].append((x, y))
                visit[(x, y)].append((nx, ny))
            elif (nx, ny) not in visit: # �湮���� ���� ���
                visit[(nx, ny)].append((x, y))
                visit[(x, y)].append((nx, ny)) # ��� ��ġ�� ���� ���� ���� �ʿ� ����
            x, y = nx, ny # �̵�
    return answer

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))