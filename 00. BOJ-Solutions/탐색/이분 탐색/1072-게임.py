import sys
input = sys.stdin.readline

def binary_search(X, Y, Z):
    answer = sys.maxsize
    left, right = 1, X
    while left <= right:
        mid = (left + right) // 2
        z = (Y + mid) * 100 // (X + mid)
        if z > Z:
            answer = min(mid, answer)
            right = mid - 1
        else:
            left = mid + 1
    return answer

X, Y = map(int, input().split())
Z = (Y * 100) // X
answer = binary_search(X, Y, Z)
print(-1 if answer == sys.maxsize else answer)