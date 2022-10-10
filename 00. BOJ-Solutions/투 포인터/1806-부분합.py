import sys
input = sys.stdin.readline
N, S = map(int, input().split())
array = list(map(int, input().split()))
i, j = 0, 0
_sum = array[i]
answer = sys.maxsize

while True:
    if _sum >= S:
        _sum -= array[i]
        answer = min(answer, j-i+1)
        i += 1
    else:
        j += 1
        if j == N:
            break
        _sum += array[j]

if answer == sys.maxsize:
    print(0)
else:
    print (answer)