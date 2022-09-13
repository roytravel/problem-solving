import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))

for i in range(len(array)-1):
    array[i+1] += array[i]

array.insert(0, 0)

for _ in range(M):
    a, b = map(int, input().split())
    print(array[b] - array[a-1])