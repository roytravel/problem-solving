import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())

if a == b == c:
    prize = 10000 + a * 1000

elif a != b and a != c and b != c:
    prize = max(a, b, c) * 100

elif a == b or b == c or a == c:
    if a == b:
        prize = 1000 + a * 100
    elif a == c:
        prize = 1000 + a * 100
    elif b == c:
        prize = 1000 + b * 100
print (prize)