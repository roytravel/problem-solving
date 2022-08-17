import math
import os
import random
import re
import sys

def arrayManipulation(n, queries):
    array = [0] * (n+1)
    for a, b, k in queries:
        start, end = a-1, b
        array[start] += k
        array[end] -= k
    
    answer = -1
    total = 0
    for i in range(len(array)):
        total = total + array[i]
        if total > answer:
            answer = total
    return answer


# Time over
# def arrayManipulation(n, queries):
#     array = [0] * (n+1)
#     for i in range(len(queries)):
#         a, b, k = queries[i]
#         for j in range(a, b+1):
#             array[j] += k
#     return max(array)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    print (result)
