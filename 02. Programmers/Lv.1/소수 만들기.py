import math
from itertools import combinations

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    candidate = []
    combination = combinations(nums, 3)
    for result in combination:
        candidate.append(sum(result))
    
    for num in candidate:
        flag = is_prime(num)
        if flag:
            answer += 1
    return answer