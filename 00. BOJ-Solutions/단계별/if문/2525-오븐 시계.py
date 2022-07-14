import sys
input = sys.stdin.readline
A, B = map(int, input().split())
C = int(input())

Q, R = divmod(C, 60)
A += Q
B = B + R

Q, R= divmod(B, 60)
A += Q
B = R

if A >= 24:
    A = A - 24

print (A, B)