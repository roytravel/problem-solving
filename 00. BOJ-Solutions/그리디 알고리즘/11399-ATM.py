# wrong answer
# from itertools import permutations
# N = int(input())
# times = list(map(int, input().split()))
# result = permutations(times, N)
# global_values = []
# for nums in result:
#     _sum = 0
#     local_values = []
#     for num in nums:
#         _sum = _sum + num
#         local_values.append(_sum)
#     global_values.append(sum(local_values))
# print (min(global_values))

N = int(input())
lines = list(map(int, input().split()))
lines = sorted(lines)
_sum = 0
times = []
for num in lines:
    _sum = _sum + num
    times.append(_sum)
print (sum(times))