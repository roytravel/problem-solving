def recursion(start):
    if M == len(picked):
        print (*picked)
        return
    
    for i in range(start, N):
        picked.append(i+1)
        recursion(start)
        picked.pop()
        start += 1

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    picked = []
    recursion(0)