#!/bin/python3
import math
import os
import random
import re
import sys

def maxMin(k, arr):
    # arr.sort()
    # result = arr[k-1] - arr[0]
    # for i in range(n-k+1):
    #     if arr[i+k-1] - arr[i] < result:
    #         result = arr[i+k-1] - arr[i]
    # return result
    k-=1
    arr.sort()
    result = sys.maxsize
    for i in range(len(arr)-k):
        result = min(result, arr[i+k]-arr[i])
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)
    result = maxMin(k, arr)
    fptr.write(str(result) + '\n')

    fptr.close()
