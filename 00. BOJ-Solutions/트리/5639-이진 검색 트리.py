<<<<<<< HEAD
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
preorder = []
=======
# import sys
# input = sys.stdin.readline
# preorder = []
>>>>>>> f2c6a25018f16071d7065871fea91c019f24ea3e

# while True:
#     try:
#         preorder.append(int(input()))
#     except:
#         break

<<<<<<< HEAD
def postorder(start, end):
    """ [50, 30, 24, 5, 28, 45, 98, 52, 60] """
    """ [5, 28, 24, 45, 30, 60, 52, 98, 50] """
    if start > end: # 시작과 끝이 역전되면 종료
        return

    mid = end + 1
    for i in range(start+1, end+1): # 서브트리 찾기
        if preorder[start] < preorder[i]: # 부모보다 크다면 오른쪽 서브 트리
            mid = i
            break
    postorder(start+1, mid-1) # 왼쪽 서브트리 재귀 탐색
    postorder(mid, end) # 오른쪽 서브트리 재귀 탐색
    print(preorder[start])

postorder(0, len(preorder)-1)
=======
# def postorder(start, end):
#     # 시작과 끝이 역전되면 종료
#     if start > end:
#         return

#     mid = end + 1
#     # 서브트리 찾기
#     for i in range(start+1, end+1):
#         # 부모보다 크다면 오른쪽 서브 트리
#         if preorder[start] < preorder[i]:
#             mid = i
#             break
    
#     postorder(start+1, mid-1)
#     postorder(mid, end)
#     print(preorder[start])

# postorder(0, len(preorder)-1)

>>>>>>> f2c6a25018f16071d7065871fea91c019f24ea3e
