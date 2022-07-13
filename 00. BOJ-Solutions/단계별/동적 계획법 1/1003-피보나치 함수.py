import sys
input = sys.stdin.readline

zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(N):
    length = len(zero)
    if N >= length:
        for i in range(length, N+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print (f"{zero[N]} {one[N]}")

T = int(input())
for i in range(T):
    N = int(input())
    fibonacci(N)