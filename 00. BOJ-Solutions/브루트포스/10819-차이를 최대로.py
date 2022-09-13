import sys
from itertools import permutations

def get_permutations(): 
    if len(picked) == N:
        _sum = 0
        for i in range(2, len(picked) +1):
            _sum += abs(picked[i-2] - picked[i-1])
        sums.append(_sum)
        return

    for i in range(len(A)):
        if visited[i]:
            continue

        visited[i] = 1
        picked.append(A[i])
        get_permutations()
        picked.pop()
        visited[i] = 0


def get_max_value(A): # Solution 1
    _main = 0
    all_cases = list(permutations(A, len(A)))
    for case in all_cases:
        _sub = 0
        for i in range(2, len(case)+1):
            _sub += abs(case[i-2] - case[i-1])
        _main = max(_sub, _main)
    return _main

if __name__ == "__main__":
    # Common
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))

    # Solution 1
    # _sum = get_max_value(A)
    # print (_sum)

    # Solution 2
    picked, sums = [], []
    visited = [0] * N
    get_permutations()
    print(max(sums))