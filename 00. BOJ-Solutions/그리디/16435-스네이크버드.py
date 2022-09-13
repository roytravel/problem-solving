import sys
input = sys.stdin.readline

N, L = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
answer = L

for height in array:
    if height <= answer:
        answer += 1
    else:
        break

print (answer)