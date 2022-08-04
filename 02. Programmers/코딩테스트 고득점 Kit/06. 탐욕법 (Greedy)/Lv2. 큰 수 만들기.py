"""
"1924"	        2	"94"
"1231234"	    3	"3234"
"4177252841"	4	"775841"
"""
import sys
input = sys.stdin.readline

def solution(numbers, k):
    numbers = list(numbers)
    result = [numbers.pop(0)]
    for num in numbers:
        if result[-1] < num:
            while result and result[-1]<num and k>0:
                result.pop()
                k -= 1
            result.append(num)
        elif k==0 or result[-1] >= num:
            result.append(num)
    if k:
        result = result[:-k]
    answer = ''.join(result)
    return answer

def solution(number, k):
    answer = [] # Stack
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    return ''.join(answer[:len(answer) - k])