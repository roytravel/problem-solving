def recursion(start):
    if M == len(picked):
        print (*picked)
        return

    for i in range(start, len(numbers)):
        picked.append(numbers[i])
        recursion(i)
        picked.pop()

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    numbers.sort()
    picked = []
    
    recursion(0)