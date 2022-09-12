import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    horse = []
    for i in range(2):
        horse.append(input())
    
    countW, countB = 0, 0
    for i in range(N):
        if horse[0][i] != horse[1][i]:
            if horse[0][i] == "W":
                countW += 1
            elif horse[0][i] == "B":
                countB += 1
    print (max(countW, countB))