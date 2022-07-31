from itertools import permutations

def check_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    primes = []
    for i in range(1, len(numbers)+1):
        permutation = permutations(numbers, i)
        for i in list(permutation):
            num = ""
            for j in i:
                num += j
            num = int(num)
            flag = check_prime(num)
            if flag:
                primes.append(num)
    primes = list(set(primes))
    return len(primes)