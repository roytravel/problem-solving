import sys
from itertools import combinations
input = sys.stdin.readline

equation = input().rstrip()
stack = []
index = []
answer = set()

for idx, value in enumerate(equation):
    if value == "(":
        stack.append(idx)
    elif value == ")":
        start = stack.pop()
        end = idx
        index.append([start, end])

for i in range(1, len(index)+1):
    combination = combinations(index, i)
    for comb in combination:
        result = list(equation)
        for c in comb:
            start, end = c
            result[start] = ''
            result[end] = ''
        answer.add(''.join(result))

for i in sorted(list(answer)):
    print (i)