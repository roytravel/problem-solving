import sys
input = sys.stdin.readline
"""
    equation
    - nCr = n! / (n-r)!r!
    example
    5C2 = 5! / (5-2)!2!
"""

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    return n * factorial(n-1)

N, K = map(int, input().split())
num = 1000000007
coefficient = factorial(N) / (factorial(N-K) * factorial(K))
print (int(coefficient % num))