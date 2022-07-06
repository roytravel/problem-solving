import os
import sys

def minimumAbsoluteDifference(arr):
    # partially correct
    # _sum = []
    # for i in range(n):
    #     for j in range(i+1, n):
    #         _sum.append(abs(arr[i] - arr[j]))
    # return min(_sum)

    # solution
    arr.sort()
    value = sys.maxsize
    for i in range(len(arr)-1):
        value = min(value, abs(arr[i] - arr[i+1]))

    return value
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()