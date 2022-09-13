import sys
inptu = sys.stdin.readline

N, M = map(int, input().split())
memo = dict()

for _ in range(N):
    site, password = map(str, input().strip().split())
    memo[site] = password

for _ in range(M):
    site = input().strip()
    print (memo[site])