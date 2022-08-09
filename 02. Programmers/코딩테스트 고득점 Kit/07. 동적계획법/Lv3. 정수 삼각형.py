def solution(triangle):
    answer = 0
    triangle = [[0] + tri + [0] for tri in triangle]
    for i in range(1, len(triangle)):
        for j in range(1, i+2):
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    answer = max(triangle[-1])
    return answer