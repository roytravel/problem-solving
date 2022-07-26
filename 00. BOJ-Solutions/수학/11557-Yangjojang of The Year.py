"""
2
3
Yonsei 10
Korea 10000000
Ewha 20
2
Yonsei 1
Korea 10000000
"""
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
    print (temp)
    print (temp[0][0])
 