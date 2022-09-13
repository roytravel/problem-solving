import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    height, width, num = map(int, input().split())

    floor = num % height
    n = (num // height) + 1
    
    if floor == 0:
        floor = height
        n -= 1
    print (floor*100+n)