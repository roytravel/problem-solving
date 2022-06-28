import sys
from math import factorial

def solution_manual(n):
    if n == 0:
        return 1

    if n == 1:
        return 1
    
    return n * solution_manual(n-1)

if __name__ == "__main__":
    input = sys.stdin.readline

    N, K = list(map(int, input().split()))
    
    # 1. library
    #print (factorial(N) // (factorial(K) * factorial(N-K)))

    # 2. solution_manual
    print (solution_manual(N) // (solution_manual(K) * solution_manual(N-K)))