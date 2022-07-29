from collections import Counter

def solution(nums):
    dictionary = Counter(nums)
    
    # Counter의 종류 세기
    n_types = len(dictionary.items())
    
    if sum(dictionary.values())//2 > n_types:
        return n_types
    else:
        return sum(dictionary.values())//2