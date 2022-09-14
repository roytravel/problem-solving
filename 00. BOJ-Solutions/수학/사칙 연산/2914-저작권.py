import sys
input = sys.stdin.readline
A, l = list(map(int, input().split()))
print ((A * l - A)+1)