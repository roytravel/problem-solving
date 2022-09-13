N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = 0

A = sorted(A)
B = sorted(B, reverse=True)

for idx in range(N):
    s = A[idx] * B[idx]
    S = S + s

print (S)