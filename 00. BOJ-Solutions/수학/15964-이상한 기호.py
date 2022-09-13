import sys
input = sys.stdin.readline
a, b = map(int, input().split())
equation = lambda x,y : (x+y)*(x-y)
print (equation(a, b))