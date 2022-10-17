import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break

    start, end = 1, 50
    while True:
        mid = (start + end) // 2
        print (mid, end = ' ')
        if mid == N:
            break
        elif mid > N:
            end = mid - 1
        else:
            start = mid + 1
    print ('')