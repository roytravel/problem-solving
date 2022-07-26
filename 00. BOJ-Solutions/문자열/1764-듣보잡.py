import sys
input = sys.stdin.readline
N, M = map(int, input().split())

hear = []
see = []

for _ in range(N):
    hear.append(input().rstrip())

for _ in range(M):
    see.append(input().rstrip())

result = set(hear).intersection(see)
result = sorted(result)
print (len(result))
for i in result:
    print (i)