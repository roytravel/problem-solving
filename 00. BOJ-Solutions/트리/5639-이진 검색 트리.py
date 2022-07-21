# import sys
# input = sys.stdin.readline
# preorder = []

# while True:
#     try:
#         preorder.append(int(input()))
#     except:
#         break

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

