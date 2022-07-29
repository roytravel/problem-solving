def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True) # 999, 555, 343434, 303030, 333
    answer = str(int(''.join(numbers)))
    return answer

# time over
# from itertools import permutations
# def solution(numbers):
#     answer = ''
#     permutation = permutations(numbers, len(numbers))
#     candidate = []
#     for result in list(permutation):
#         temp = ""
#         for i in result:
#             temp += str(i)
#         candidate.append(int(temp))
#     return str(max(candidate))