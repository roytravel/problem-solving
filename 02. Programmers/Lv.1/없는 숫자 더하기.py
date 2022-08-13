def solution(numbers):
    answer = 0
    for i in range(1, 9+1):
        if not numbers.count(i):
            answer += i
    return answer