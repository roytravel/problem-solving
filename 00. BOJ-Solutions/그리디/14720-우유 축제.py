import sys
input = sys.stdin.readline
N = int(input())
milk = list(map(int, input().split())) # 0: strawberry, 1: chocolate, 2: banana
count = 0
target = 0
for i in range(N):
    if milk[i] == target:
        target += 1
        if target == 3:
            target = 0
        count += 1
print(count)