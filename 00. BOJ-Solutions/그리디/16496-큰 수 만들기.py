"""
5
3 30 34 5 9
-----
9534330

5
0 0 0 0 1
10000
"""

import sys
input = sys.stdin.readline
N = int(input())
array = list(map(str, input().split()))
array.sort(key=lambda x:x*10, reverse=True)
answer = ""
for i in array:
    answer += str(int(i))
print (int(answer))