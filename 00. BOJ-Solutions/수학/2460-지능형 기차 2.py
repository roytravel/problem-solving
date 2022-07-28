import sys
input = sys.stdin.readline

array = []
start = 0
for _ in range(10):
    A, B = map(int, input().split())
    start = start - A + B
    array.append(start)

print (max(array))