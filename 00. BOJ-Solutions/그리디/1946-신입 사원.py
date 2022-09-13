import sys
input = sys.stdin.readline

T = int(input())
score = []
    
for _ in range(T):
    N = int(input())
    count = 1
    top = 0
    score = [list(map(int, input().split())) for _ in range(N)]
    score = sorted(score)
    
    for i in range(1, len(score)):
        if score[i][1] < score[top][1]:
            top = i
            count += 1
    print (count)