""" reference: https://velog.io/@bae_mung/Python-BOJ-2263-트리의-순회 """
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# 분할 정복 방식으로 전위 순회를 찾음
def get_preorder(in_start, in_end, post_start, post_end):
    if(in_start > in_end) or (post_start > post_end):
        return

    # 후위 순회 결과 끝 = 루트 노드임을 이용 
    parents = postorder[post_end]
    preorder.append(parents)

    # 중위 순회에서 루트 좌우로 트리가 갈라지는 것을 이용해 left, right를 선언
    left = position[parents] - in_start
    right = in_end - position[parents]

    # left, right로 나눠 분할 정복 방식으로 트리를 추적해 전위 순회를 찾음
    get_preorder(in_start, in_start+left-1, post_start, post_start+left-1) # left sub-tree
    get_preorder(in_end-right+1, in_end, post_end-right, post_end-1) # right sub-tree

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 후위 순회의 끝값이 중위 순회의 어디 인덱스에 위치한지 확인을 위해
# 중위 순회의 값들의 인덱스값을 저장
position = [0]*(n+1)
for i in range(n):
    position[inorder[i]] = i

# 중위 순회, 후위 순회 모두 0부터 n-1 (전체 범위)값을 주고 전위 순회를 구함
preorder = []
get_preorder(0, n-1, 0, n-1)
print (*preorder, end=' ')

"""
7
4 2 5 1 6 3 7
4 5 2 6 7 3 1
==============
1 2 4 5 3 6 7
"""