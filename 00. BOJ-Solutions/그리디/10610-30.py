N = list(input())
N.sort(reverse=True)
SUM = 0
for i in N:
    SUM += int(i)
if SUM % 3 != 0 or "0" not in N:
    print (-1)
else:
    print ("".join(N))


# Time over
# import sys
# from itertools import permutations
# input = sys.stdin.readline

# N = input().strip()
# num = list(N)
# permutation = permutations(num, len(num))
# array = []

# for perm in permutation:
#     target = int(''.join(perm))
#     if target % 30 == 0:
#         array.append(target)

# if array:
#     print (max(array))
# else:
#     print (-1)