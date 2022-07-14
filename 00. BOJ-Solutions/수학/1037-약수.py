# failed
import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
MAX = 1000000
for i in range(max(nums)*2, MAX+1):
    flag = True
    for j in nums:
        if i % j == 0:
            continue
        else:
            flag = False
    if flag == False:
        continue
    else:
        print (i)
        break