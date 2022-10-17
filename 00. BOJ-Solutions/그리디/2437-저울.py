import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
array.sort()
target = 1
for num in array:
    if target < num:
        break
    target += num
print (target)

# memory over
# import sys
# from itertools import combinations
# N = int(input())
# array = list(map(int, input().split()))

# candidate = []
# for i in range(1, N+1):
#     combination = combinations(array, i)
#     for comb in combination:
#         candidate.append(sum(comb))

# candidate = list(set(candidate))
# candidate.sort()

# for i in range(1_000_001):
#     if candidate[i] != i+1:
#         print (i+1)
#         break
