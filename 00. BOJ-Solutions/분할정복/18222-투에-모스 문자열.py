import sys
input = sys.stdin.readline

def make_thue_morse(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    if N % 2:
        return 1-make_thue_morse(N//2)
    else:
        return make_thue_morse(N//2)

N = int(input())
print(make_thue_morse(N-1))