import sys
T = int(input())
for _ in range(T):
    count, string = sys.stdin.readline().split()
    P = ""
    for s in range(len(string)):
        P += string[s] * int(count)
        if s == len(string) -1:
            print (P)