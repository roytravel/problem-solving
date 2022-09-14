import sys
from collections import deque
input = sys.stdin.readline

def D(n):
    n = n * 2
    if n > 9999:
        n %= 10000
    return n
    
def S(n):
    if n == 0:
        n = 9999
    else:
        n -= 1
    return n

def L(n):
    front = n % 1000
    back = n // 1000
    n = front*10 + back
    return n

def R(n):
    front = n % 10
    back = n // 10
    n = front * 1000 + back
    return n


T = int(input())
for _ in range(T):
    src, dst = map(int, input().split())
    queue = deque()
    visited = set() # log n
    queue.append([src, ""])
    visited.add(src)

    while queue:
        num, cmd = queue.popleft()
        if num == dst:
            print (cmd)
            break

        n = D(num)
        if n not in visited:
            visited.add(n)
            queue.append([n, cmd+"D"])
        
        n = S(num)
        if n not in visited:
            visited.add(n)
            queue.append([n, cmd+"S"])
        
        n = L(num)
        if n not in visited:
            visited.add(n)
            queue.append([n, cmd+"L"])
        
        n = R(num)
        if n not in visited:
            visited.add(n)
            queue.append([n, cmd+"R"])