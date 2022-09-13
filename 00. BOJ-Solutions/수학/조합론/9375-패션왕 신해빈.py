import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    clothes = []
    for __ in range(n):
        a, b = input().split()
        clothes.append(b)
    
    clothe = Counter(clothes)    
    count = 1
    for key in clothe.keys():
        count *= clothe[key] + 1
    print (count-1)