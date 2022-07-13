import sys


def tetromino1():
    pass

def get_max_score():

    # 가로 막대기
    len_horizontal_bar = 4
    local_scores = []
    global_scores = []
    for i in range(N): # 행
        for j in range(M - len_horizontal_bar + 1): #열
            local_scores.append(sum(paper[i][j:j+len_horizontal_bar]))

    print (local_scores)
    global_scores.append(max(local_scores))

    
    # 정사각형
    square_width = 2
    square_height = 2
    dx = [1, 0, 1]
    dy = [0, 1, 1]
    score = 0
    local_scores = []
    for i in range(N - square_width + 1):
        for j in range(M - square_height + 1):
            score += paper[i][j]
            for _ in range(3):
                new_i = i + dx[_]
                new_j = j + dy[_]
                score += paper[new_i][new_j]
            local_scores.append(score)
            score = 0
    
    print (local_scores)
    global_scores.append(max(local_scores))

    # L 모양
    score = 0
    local_scores = []
    for i in range(N-2): # 0, 1, 2
        for j in range(M-2+1):
            score += paper[i][j]
            score += paper[i+1][j]
            score += paper[i+2][j]
            score += paper[i+2][j+1]
            local_scores.append(score)
            score = 0
    
    print (local_scores)
    global_scores.append(max(local_scores))

    # "녹" 모양
    score = 0
    local_scores = []
    for i in range(N - 2): # 0, 1, 2, 3
        for j in range(M - 2 + 1): # 0, 1, 2
            score += paper[i][j]
            score += paper[i+1][j]
            score += paper[i+1][j+1]
            score += paper[i+2][j+1]
            local_scores.append(score)
            score = 0
    
    print (local_scores)
    global_scores.append(max(local_scores))

    # "ㅜ" 모양
    score = 0
    local_scores = []
    for i in range(N - 2 + 1): # 5-3+1 = 0~3 = 0, 1, 2
        for j in range(M - 2): # 5-2+1 = [0-4) = 0,1,2,3
            score += paper[i][j]
            score += paper[i][j+1] + paper[i][j+2]
            score += paper[i+1][j+1]
            
            local_scores.append(score)
            score = 0
    print (local_scores)

    global_scores.append(max(local_scores))

    print (max(global_scores))


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = list(map(int, input().split()))
    
    paper = []

    for _ in range(N):
        paper.append(list(map(int, input().split())))

    get_max_score()