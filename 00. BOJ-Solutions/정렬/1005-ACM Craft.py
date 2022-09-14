import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, K = map(int, input().rstrip().split())
    time = list(map(int, input().rstrip().split()))
    graph = [[] for _ in range(N+1)]
    in_degree = [0 for _ in range(N+1)]
    dp = [0 for _ in range(N+1)]
    queue = deque()

    for i in range(K):
        src, dst = map(int, input().rstrip().split())
        graph[src].append(dst)
        in_degree[dst] += 1

    W = int(input().rstrip())

    for i in range(1, N+1):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = time[i-1]

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            in_degree[i] -= 1
            dp[i] = max(dp[i], dp[now]+time[i-1])
            if in_degree[i] == 0:
                queue.append(i)
    print(dp[W])