import sys
input = sys.stdin.readline
N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

def pooling(array, N):
    if N == 1:
        return array[0][0]
    new_array = [[] for _ in range(N//2)]
    for i in range(0, N, 2):
        for j in range(0, N, 2):
            new_array[i//2].append(sorted([array[i][j], array[i][j+1], array[i+1][j], array[i+1][j+1]])[2])
    return pooling(new_array, N//2)

print (pooling(array, N))