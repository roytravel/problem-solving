import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
time , height = sys.maxsize, 0

for target in range(257):
    min, max = 0, 0    
    for i in range(N):
        for j in range(M):
            if ground[i][j] >= target:
                max += ground[i][j] - target
            else:
                min += target - ground[i][j]

    inventory = max + B
    if inventory >= min:
        temp = max*2 + min
        if temp <= time:
            time = temp
            height = target

print (time, height)