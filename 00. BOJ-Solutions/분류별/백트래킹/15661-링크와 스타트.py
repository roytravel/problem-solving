import sys

def get_minimum_diff(idx, count):
    if count >= N // 2:
        global result
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if selected[i] and selected[j]:
                    start += score[i][j]
                elif not selected[i] and not selected[j]:
                    link += score[i][j]
        result = min(result, abs(start - link))

    for i in range(idx, N):
        if selected[i]:
            continue

        selected[i] = 1
        get_minimum_diff(i+1, count+1)
        selected[i] = 0

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    input = sys.stdin.readline
    N = int(input())
    score = [list(map(int, input().split())) for _ in range(N)]
    result = sys.maxsize
    selected = [0 for _ in range(N)]
    get_minimum_diff(0, 0)
    print (result)