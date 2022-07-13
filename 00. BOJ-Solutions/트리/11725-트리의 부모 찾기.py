import sys
input = sys.stdin.readline
N = int(input())

tree = {}

for _ in range(N-1):
    left, right = list(map(int, input().split()))
    tree[left] = right


print (tree)
