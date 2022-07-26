import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
deq = deque([i for i in range(1, N+1)])
count = 0 

for i in array:
    while True:
        if deq[0] == i:
            deq.popleft()
            break
        else:
            if deq.index(i) <= len(deq) // 2:
                deq.rotate(-1)
                count += 1
            else:
                deq.rotate(1)
                count += 1
print (count)