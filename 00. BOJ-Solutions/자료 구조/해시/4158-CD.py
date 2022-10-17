import sys
from collections import defaultdict
input = sys.stdin.readline

while True:
    CD = defaultdict(bool)
    N, M = map(int, input().split())
    count = 0
    if (N, M) == (0, 0):
        break
    for _ in range(N):
        CD[int(input())] = True

    for _ in range(M):
        if CD[int(input())]:
            count += 1

    print(count)