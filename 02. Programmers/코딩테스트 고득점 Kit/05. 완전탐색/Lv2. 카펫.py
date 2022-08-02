def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for a in range(total, 2, -1):
        if total % a == 0:
            b = total // a
            if yellow == (b-2)*(a-2):
                return [a, b]