# -*- coding:utf-8 -*-
import sys
input = sys.stdin.readline
N = int(input())

paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))

result = []
def solution(x, y, N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

solution(0, 0, N)
print (result.count(0))
print (result.count(1))

# import sys
# input = sys.stdin.readline
# N = int(input())
# board = []
# for i in range(N):
#     board.append(list(map(int, input().split())))

# # ��ü ���� ��� ������ ����
# def check_all_colors(part):
#     temp = []
#     for i in range(N):
#         for j in range(N):
#             temp.append(part[i][j])
#             if 1 in temp and 0 in temp:
#                 del temp # deallocate
#                 return False
#     return True

# # ������ �ΰ� �ٸ��� 4���� �ϱ�
# def split_four_parts(part):
#     length = len(part[0]) // 2
#     parts = [[] * length for _ in range(length)]
#     for i in range(length): # 1
#         for j in range(length):
#             parts[i][j] = part[i][j]
    
#     for i in range(length): # 2
#         for j in range(length, length*2):
#             parts[i][j] = part[i][j]

#     for i in range(length, length*2): # 3
#         for j in range(length):
#             parts[i][j] = part[i][j]
    
#     for i in range(length, length*2): # 4
#         for j in range(length, length*2):
#             parts[i][j] = part[i][j]

#     return parts


# # ���̻� �ڸ��� ���Ҷ�����

# while True:
#     BOOL = check_all_colors(board)
#     if BOOL:
#         split_four_parts(board)
#     else: