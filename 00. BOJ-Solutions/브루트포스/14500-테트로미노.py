import sys
input = sys.stdin.readline

# ㅗ, ㅜ, ㅓ, ㅏ 모양 제외 최대값 계산
def dfs(x, y, dsum, count):
    global MAX
    if count == 4:
        MAX = max(MAX, dsum)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, dsum + graph[nx][ny], count+1)
            visited[nx][ny] = False


# ㅗ, ㅜ, ㅓ, ㅏ 모양 최대값 계산
def get_max_value(x, y):
    global MAX
    for i in range(4):
        temp = graph[x][y] 
        for k in range(3):
            t = (i+k)%4 # dir 배열 요소를 3개씩 사용할 수 있도록 인덱스 계산 # 012, 123, 230, 301
            nx = x + dx[t]
            ny = y + dy[t]
            if not (0<=nx<N and 0<=ny<M):
                temp = 0
                break
            temp += graph[nx][ny]
        MAX = max(MAX, temp)


if __name__ == "__main__":
    MAX = 0
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i, j, graph[i][j], 1)
            visited[i][j] = False
            get_max_value(i, j)
    print(MAX)