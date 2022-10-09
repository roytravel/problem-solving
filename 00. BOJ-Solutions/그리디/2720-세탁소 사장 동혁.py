import sys
input = sys.stdin.readline
quarter = 0.25 * 100
dime = 0.1 * 100
nickel = 0.05 * 100
penny = 0.01 * 100
T = int(input())
for _ in range(T):
    coin = 0
    N = int(input())
    a, R = divmod(N, quarter)
    b, R = divmod(R, dime)
    c, R = divmod(R, nickel)
    d, R = divmod(R, penny)
    print (*map(int, [a, b, c, d]))