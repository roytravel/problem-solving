import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
queue = deque(enumerate(map(int, input().split())))
while queue:
    idx, num = queue.popleft()
    print(idx+1, end=' ')
    if num > 0:
        queue.rotate(-(num-1))
    elif num < 0:
        queue.rotate(-num)