import sys
input = sys.stdin.readline
n1, n2, n3 = map(int, input().split())
print (int((n1+1)*(n2+1)/(n3+1)-1))