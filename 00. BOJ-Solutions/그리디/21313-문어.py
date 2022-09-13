import sys
input = sys.stdin.readline

N = int(input())
prefix = "12"
answer = ""

if N % 2 == 0: # the case when N is even
    answer = prefix * (N//2)
else: # the case when N is odd
    answer = prefix * (N//2) + "3"

print (*map(int, list(answer)))