import sys
from itertools import permutations

input = sys.stdin.readline
k = int(input())
inequal_sign = list(input().split())
max_value = pow(10, k+1) - 1
candidate = list()
nums = list(permutations([i for i in range(10)], k+1))
reversed_nums = reversed(nums)

for num in reversed_nums:
    if len(num) != len(set(num)):
        continue

    for n in range(len(num)-1):
        if inequal_sign[n] == "<":
            if not num[n] < num[n+1]:
                break
            
        elif inequal_sign[n] == ">":
            if not num[n] > num[n+1]:
                break
    else:
        candidate.append(num)
        break

for num in nums:
    if len(num) != len(set(num)):
        continue

    for n in range(len(num)-1):
        if inequal_sign[n] == "<":
            if not num[n] < num[n+1]:
                break
            
        elif inequal_sign[n] == ">":
            if not num[n] > num[n+1]:
                break
    else:
        candidate.append(num)
        break

print ("".join(map(str, list(candidate[0]))))
print ("".join(map(str, list(candidate[1]))))