import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
S = list(map(int, input().split()))
start, end = 0, 0
size, max_size = 0, 0
count = 0
flag = True

for start in range(N):
    while count <= K and flag:
        if S[end] % 2:
            if count == K:
                break
            count += 1
        size += 1

        if end == N - 1:
            flag = False
            break
        end += 1

    if max_size < size - count:
        max_size = size - count

    if S[start] % 2:
        count -= 1
    
    size -= 1

print (max_size)