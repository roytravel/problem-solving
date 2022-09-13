import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    J, N = map(int, input().split())
    size = []
    for i in range(N):
        r, c = map(int, input().split())
        size.append(r*c)
    
    size.sort(reverse=True)
    count = 0
    for s in size:
        J = J - s
        count += 1
        if J <= 0:
            break 
    print (count)