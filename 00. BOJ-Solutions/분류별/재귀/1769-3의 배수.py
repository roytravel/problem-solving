def is_multiple_of_three(N, cnt):
    if len(N) == 1:
        if int(N) % 3 == 0:
            print (cnt)
            print ("YES")
        else:
            print (cnt)
            print ("NO")
        return
    
    _sum = 0
    for i in N:
        _sum += int(i)
    
    is_multiple_of_three(str(_sum), cnt+1)

if __name__ == "__main__":
    N = input()
    is_multiple_of_three(N, 0)