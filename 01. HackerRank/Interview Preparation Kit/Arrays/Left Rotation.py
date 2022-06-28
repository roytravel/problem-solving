import os
from collections import deque

def rotLeft(a, d):
    queue = deque(a)
    for _ in range(d):
        num = queue.popleft()
        queue.append(num)
    
    return queue

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()