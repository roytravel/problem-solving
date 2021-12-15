def combination(start):
    if len(picked) == M:
        print (*picked)
        return
    
    for i in range(start, len(array)):
        picked.append(array[i])
        combination(i)
        picked.pop()        

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    array = list(map(int, input().split()))
    array = sorted(list(set(array)))
    picked = []
    combination(0)