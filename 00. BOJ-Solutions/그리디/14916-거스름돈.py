import sys
input = sys.stdin.readline
n = int(input())
Q1, R1 = divmod(n, 5)
while True:
    if R1 % 2 == 0:
        Q2, R2 = divmod(R1, 2)
        print (Q1 + Q2)
        break
    else:
        Q1 = Q1 - 1
        R1 = R1 + 5 
    
    if Q1 < 0:
        print (-1)
        break