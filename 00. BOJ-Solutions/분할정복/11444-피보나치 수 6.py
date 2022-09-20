import sys
input = sys.stdin.readline

def power(a: list, b: int) -> list:
    if b == 1:
        return a
    else:
        mat = power(a, b//2)  # a^(b//2)
        if b % 2 == 0:
            return matmul(mat, mat)
        else:
            return matmul(matmul(mat, mat), a)

def matmul(mat1: list, mat2: list) -> list:
    matrix = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                matrix[i][j] += (mat1[i][k] * mat2[k][j]) % mod
    return matrix

N = int(input())
adj = [[1, 1], 
       [1, 0]]
mod = 1000000007
matrix = power(adj, N)
print(matrix[0][1] % mod)