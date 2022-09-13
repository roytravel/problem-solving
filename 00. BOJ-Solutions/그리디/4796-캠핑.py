import sys
input = sys.stdin.readline

cnt = 0
while True:
    day = 0
    L, P, V = map(int, input().split())
    if (L, P, V) == (0, 0, 0):
        break

    cnt += 1
    day += (V // P) * L
    day += min(V % P, L)
    print (f"Case {cnt}: {day}")