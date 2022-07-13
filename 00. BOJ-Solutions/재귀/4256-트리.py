import sys
from itertools import permutations

input = sys.stdin.readline

def preorder_traversal(i, something):
    if something > len(i):
        return

    print (something, end =' ')
    preorder_traversal(i, 2*something)
    preorder_traversal(i, 2*something+1)


T = int(input())

for _ in range(T):
    length = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    element = list(set(preorder))
    result = permutations(element, len(element))
    for i in result:
        print ('start', i)
        preorder_traversal(i, 1)
        print()
