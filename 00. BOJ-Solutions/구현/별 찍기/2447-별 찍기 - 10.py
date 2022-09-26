import sys
sys.setrecursionlimit(10**9)

def star(N):
    if N == 1:
        return ['*']

    stars = star(N//3)
    print (N, stars)
    l = []
    for s in stars:
        l.append(s*3)
    for s in stars:
        l.append(s+" "*(N//3)+s)
    for s in stars:
        l.append(s*3)
    print (N, l)
    return l
    
N = int(sys.stdin.readline().strip())
print ('\n'.join(star(N)))