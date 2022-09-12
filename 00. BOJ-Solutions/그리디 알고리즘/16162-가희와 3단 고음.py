import sys
input = sys.stdin.readline

N, A, D = map(int, input().split())
array = list(map(int, input().split()))
count = 0
for n in array:
    if n == A:
        A += D
        count += 1
print (count)