import sys
input = sys.stdin.readline
K = int(input())
array = list(map(int, input().split()))
tree = [[] for _ in range(K)]

def create_tree(array, depth):
    mid = len(array) // 2
    tree[depth].append(array[mid])

    if len(array) == 1:
        return
    
    create_tree(array[:mid], depth+1) # left 
    create_tree(array[mid+1:], depth+1) # right

create_tree(array, 0)
for i in range(K):
    print (*tree[i])