def recursion():
    if len(picked) == M:
        print (*picked)
        return

    for i in range(len(array)):
        picked.append(array[i])
        recursion()
        picked.pop()

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    array = list(map(int, input().split()))
    array = sorted(list(set(array)))
    picked = []
    recursion()