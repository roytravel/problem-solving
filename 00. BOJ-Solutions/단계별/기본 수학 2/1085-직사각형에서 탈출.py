import sys
input = sys.stdin.readline
x, y ,w, h = list(map(int, input().split()))
print (min([x, w-x, h-y, y]))