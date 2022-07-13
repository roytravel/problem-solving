import sys

input = sys.stdin.readline
N = int(input())

for _ in range(N):
    ps = input()
    _sum = 0

    for i in ps:
        if i == "(":
            _sum +=1
        elif i == ")":
            _sum -=1
        
        if _sum < 0:
            break
    
    if _sum == 0:
        print ("YES")

    else:
        print ("NO")