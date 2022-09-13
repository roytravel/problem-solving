import sys
input = sys.stdin.readline

n = int(input())
coordinate = []
for _ in range(n):
    x, y = map(int, input().split())
    coordinate.append([x, y])

x_mid = sorted(coordinate, key=lambda x:x[0])[n//2][0]
y_mid = sorted(coordinate, key=lambda x:x[1])[n//2][1]

answer = 0
for i in coordinate:
    answer += abs(x_mid-i[0]) + abs(y_mid-i[1])
print (answer)