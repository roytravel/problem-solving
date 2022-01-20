import sys

def preorder_traversal(root):
    if root != '.':
        print (root, end='')
        preorder_traversal(tree[root][0]) # left
        preorder_traversal(tree[root][1]) # right

def inorder_traversal(root):
    if root != '.':
        inorder_traversal(tree[root][0])
        print (root, end='')
        inorder_traversal(tree[root][1])


def postorder_traversal(root):
    if root != '.':
        postorder_traversal(tree[root][0])
        postorder_traversal(tree[root][1])
        print (root, end='')


input = sys.stdin.readline
N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

preorder_traversal('A')
print ()
inorder_traversal('A')
print ()
postorder_traversal('A')

