import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
queue = deque([[N]])
answer = []

while queue:
    array = queue.popleft()
    x = array[0]
    if x == 1:
        answer = array
        break

    if x % 3 == 0:
        queue.append([x//3] + array)

    if x % 2 == 0:
        queue.append([x//2] + array)
    
    queue.append([x-1] + array)

print(len(answer) - 1)
print(*answer[::-1])