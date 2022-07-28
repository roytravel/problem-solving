def GCD(A, B):
    while B:
        A, B = B, A % B
    return A

def LCM(A, B):
    return A * B // GCD(A, B)

def solution(n, m):
    answer = [GCD(n, m), LCM(n, m)]
    return answer