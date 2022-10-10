N = int(input())
A = list(map(int, input().split()))
newA = sorted(A)
P = []
for i in range(N):
    idx = newA.index(A[i])
    P.append(idx)
    newA[idx] = -1
print(*P)