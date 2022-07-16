import sys
input = sys.stdin.readline
N = int(input())
array = list(map(int, input().split()))
array.sort()
standard = 2e+9+1
left = 0
right = N-1

while left < right:
    l = array[left]
    r = array[right]
    _sum = l + r
    if abs(_sum) < standard:
        standard = abs(_sum)
        answer = [l, r]
    
    if _sum < 0:
        left += 1
    else:
        right -= 1

print (answer[0], answer[1])