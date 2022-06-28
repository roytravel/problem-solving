from itertools import combinations

def library():
    numbers.sort()
    result = list(combinations(numbers, M))
    for i in result:
        print (*i)

def recursion(start):
    if M == len(picked):
        print (*picked)
        return

    for i in range(start, len(numbers)):
        if numbers[i] not in picked:
            picked.append(numbers[i])
            recursion(i+1)
            picked.pop()

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    numbers.sort()
    picked = []
    
    recursion(0)
    #library()