import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    answer = 0
    height = (start+end)//2
    for t in tree:
        if t >= height:
            answer += t - height
    if answer >= M:
        start = height+1
    else:
        end = height-1
print (end)