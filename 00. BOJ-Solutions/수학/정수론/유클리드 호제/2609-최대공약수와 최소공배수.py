import sys
input = sys.stdin.readline
N, M = map(int, input().split())

def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

def LCM(x, y):
    result = (x*y) // GCD(x, y)
    return result

print (GCD(N, M))
print (LCM(N, M))