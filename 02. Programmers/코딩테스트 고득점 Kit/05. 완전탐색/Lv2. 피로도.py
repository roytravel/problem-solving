from itertools import permutations
from copy import deepcopy

def solution(k, dungeons):
    permutation = permutations(dungeons, len(dungeons))
    candidate = []
    for result in list(permutation):
        answer = 0
        total = deepcopy(k)
        for minimum, consume in result:
            if total >= minimum and total-consume >= 0:
                total -= consume
                answer += 1
        candidate.append(answer)
    return max(candidate)