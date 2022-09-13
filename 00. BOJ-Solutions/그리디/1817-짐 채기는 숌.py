import sys
input = sys.stdin.readline

N, M = map(int, input().split())
if N == 0:
    print (0)
    exit()

array = list(map(int, input().split()))
box = 1
weight = 0

for i in range(N-1, -1, -1):
    weight += array[i]
    if weight > M:
        box += 1
        weight = array[i]
    
print (box)