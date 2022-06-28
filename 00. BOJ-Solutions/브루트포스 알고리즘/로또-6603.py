import sys
from itertools import combinations

def dfs(start):
    if len(picked) == 6:
        print (*picked)
        return

    for i in range(start, len(test_case)):
        picked.append(test_case[i])
        dfs(i+1)
        picked.pop()

if __name__ == "__main__":
    # 1. manual dfs algorithm for combination
    input = sys.stdin.readline

    while True:
        test_case = list(map(int, input().split()))
        if len(test_case) == 1:
            break

        del test_case[0]
        picked = []
        dfs(0)
        print()

    # 2. using library for combination algorithm
    # while True:
    #     test_case = list(map(int, input().split()))
    #     del test_case[0]

    #     combination = combinations(test_case, 6)
    #     for element in combination:
    #         print (*element)

    #     print ()

    #     if not test_case:
    #         break