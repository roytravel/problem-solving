def recursion():
    if M == len(picked):
        print (*picked)
        return
    
    for i in range(N):
        picked.append(i+1)
        recursion()
        picked.pop()

if __name__ == "__main__":
    
    N, M = list(map(int, input().split()))
    picked = []
    recursion()