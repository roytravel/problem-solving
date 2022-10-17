import sys
input = sys.stdin.readline
N, M = map(int, input().split())
rect = [input() for _ in range(N)]
check = min(N, M)
answer = 0
for i in range(N):
    for j in range(M):
        for k in range(check): 
            # 모든 좌표를 돌며 k개씩 늘려가며 꼭지점 수가 같은지 판단 후 같을 경우
            if ((i+k)<N) and ((j+k)<M) and (rect[i][j] == rect[i][j+k] == rect[i+k][j] == rect[i+k][j+k]):
                answer = max(answer, (k+1)**2) # 넓이이므로 
print (answer)