import math
import os
import random
import re
import sys

def getMinimumCost(k, c):
    cost = 0
    c.sort(reverse=True)
    for i in range(len(c)):
        cost += c[i] * (i//k+1)
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    fptr.write(str(minimumCost) + '\n')
    fptr.close()