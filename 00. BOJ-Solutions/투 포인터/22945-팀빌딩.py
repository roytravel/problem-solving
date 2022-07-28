import sys
input = sys.stdin.readline
N = int(input())
ability = list(map(int, input().split()))
start = 0
end = N - 1
answer = 0
while start < end:
    answer = max(answer, (end - start - 1) * min(ability[start], ability[end]))
    if ability[start] < ability[end]:
        start += 1
    else:
        end -= 1
print (answer)