import sys
input = sys.stdin.readline 

N, r, c = map(int, input().split())

# Solution 1
def solution(N, r, c):
    if N == 0:
        return 0
    
    return 2*(r%2)+(c%2) + 4*solution(N-1, int(r/2), int(c/2))

print (solution(N, r, c))