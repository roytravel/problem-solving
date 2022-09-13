import sys
input = sys.stdin.readline
N, C = map(int, input().split())
M = int(input())
table = []

for _ in range(M):
    src, dst, weight = map(int, input().split())    
    table.append([src, dst, weight])

table.sort(key=lambda x: x[1])
capacity = [C] * (N+1)
answer = 0

for src, dst, weight in table:
    temp = C
    for i in range(src, dst):
        temp = min(temp, capacity[i])

    temp = min(temp, weight)
    
    for i in range(src, dst):
        capacity[i] -= temp

    answer += temp
print (answer)