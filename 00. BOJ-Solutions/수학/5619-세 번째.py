import sys
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))

array.sort()
result = []

if N > 4:
    N = 4

for i in range(N):
    for j in range(N):
        if i != j:
            value = int(str(array[i]) + str(array[j]))
            result.append(value)
result.sort()
print (result[2])

# Time over
# import sys
# from itertools import permutations
# input = sys.stdin.readline
# N = int(input())
# array = []
# result = []
# for _ in range(N):
#     array.append(int(input()))

# permutation = permutations(array, 2)
# for i in list(permutation):
#     value = int(str(i[0]) + str(i[1]))
#     result.append(value)

# result.sort()
# print (result[2])