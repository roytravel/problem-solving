import sys
input = sys.stdin.readline

N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))
ropes.sort(reverse=True)

values = []
for i in range(N):
    values.append(ropes[i] * (i+1))

print(max(values))