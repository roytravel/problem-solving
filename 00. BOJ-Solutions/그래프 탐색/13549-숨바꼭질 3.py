import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
MAX = 10**5 + 1
dp = [-1] * MAX
dp[N] = 0

queue = deque([N])
while queue:
    X = queue.popleft()
    if X == K:
        print (dp[K])
        break
    
    if 0<= X-1 < MAX and dp[X-1] == -1:
        dp[X-1] = dp[X] + 1
        queue.append(X-1)

    if 0 < X*2 < MAX and dp[X*2] == -1:
        dp[X*2] = dp[X]
        queue.appendleft(X*2)

    if 0 <= X+1 < MAX and dp[X+1] == -1:
        dp[X+1] = dp[X] + 1
        queue.append(X+1)