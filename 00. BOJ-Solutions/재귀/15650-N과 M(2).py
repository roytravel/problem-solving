from itertools import combinations

def dfs(start):
    if M == len(picked):
        print (*picked)
        return
    
    for i in range(start, N+1):
        if i not in picked:
            picked.append(i)
            dfs(i+1)
            picked.pop()

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    
    # method 1. using combinations in litertools library
    # array = [i+1 for i in range(N)]
    # result = list(combinations(array, M))
    # for i in result:
    #     print (*i)
    
    # method 2. using maual recursion
    picked = []
    dfs(start=1)