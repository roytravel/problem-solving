import sys
input = sys.stdin.readline   
N = int(input())
budget = list(map(int, input().split()))
estimation = int(input())
start, end = 0, max(budget)
while start<=end:
    mid = (start + end) // 2
    total = 0
    for i in budget:
        if i > mid:
            total += mid
        else:
            total += i
    if total > estimation:
        end = mid - 1
    else:
        start = mid + 1
print(end)