from itertools import permutations

def permutation():
    if len(picked) == M:
        print (' '.join(str(i) for i in picked))
        return
    else:
        for i in range(1, n+1):
            if i not in picked:
                picked.append(i)
                permutation()
                picked.pop()

if __name__ == "__main__":
    # method 1. use permutations function in itertools library.
    # N, M = list(map(int, input().split()))
    # array = [i+1 for i in range(N)]
    # result = list(permutations(array, M))
    # for i in result:
    #     print (i)

    # method 2. use manual recursion.
    N, M = list(map(int, input().split()))
    picked = []
    array = [i for i in range(N)]
    n = len(array)
    permutation()

