N = int(input())
left, right = 0, N
while left<=right:
    mid = (left+right) // 2 
    if pow(mid, 2) < N:
        left = mid + 1
    else:
        right = mid - 1
print(left)