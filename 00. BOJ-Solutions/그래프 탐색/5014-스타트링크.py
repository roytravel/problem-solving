import sys
from collections import deque
input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
visited = [-1] * (F + 1)

def bfs(source, target):
    queue = deque([source])
    visited[source] = 0
    while queue:
        x = queue.popleft()
        if x == target:
            print (visited[x])
            break
        for i in (x+U, x-D):
            if 0 < i <= F and visited[i] == -1:
                visited[i] = visited[x] + 1
                queue.append(i)

    if visited[target] == -1:
        print ("use the stairs")

bfs(S, G)

"""
F: number of all floors
S: floor that Kangho stay
G: place where startlink is
U: up
D: down
10 1 10 2 1 --> 6
"""