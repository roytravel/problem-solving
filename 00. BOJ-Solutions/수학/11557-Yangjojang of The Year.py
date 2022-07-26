import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    temp = []
    for __ in range(N):
        school, drink = input().rstrip().split()
        temp.append([school, int(drink)])
    temp.sort(key=lambda x: x[1], reverse=True)
    print (temp[0][0])