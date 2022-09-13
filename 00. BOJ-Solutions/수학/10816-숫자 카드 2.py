import sys
input = sys.stdin.readline
array = [0] * (500000+1)
N = int(input())
card = list(map(int, input().split()))
M = int(input())
given = list(map(int, input().split()))
for i in card:
    array[i] += 1

for i in given:
    print(array[i], end=' ')