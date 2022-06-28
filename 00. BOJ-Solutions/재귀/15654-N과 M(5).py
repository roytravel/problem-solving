def recursion():
    if M == len(picked):
        print (*picked)
        return

    for i in numbers:
        if i not in picked:
            picked.append(i)
            recursion()
            picked.pop()

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    numbers.sort()
    picked = []
    
    recursion()