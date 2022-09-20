import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    dist = [INF] * (n+1)
    dist[start]=0
    for i in range(n):
        for edge in edges:
            src, dst, cost = edge[0], edge[1], edge[2]
            if dist[dst] > cost + dist[src]:
                dist[dst] = cost + dist[src]
                if i == n - 1:
                    return True
    return False

t = int(input())
for _ in range(t):
    n, m, w = map(int, input().split())
    edges = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    flag = bf(1)
    if flag:
        print("YES")
    else:
        print("NO")