import os

def minimumAbsoluteDifference(arr):
    candidate = []
    arr.sort()
    for i in range(n-1):
        difference = abs(arr[i] - arr[i+1])
        candidate.append(difference)
    return min(candidate)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()