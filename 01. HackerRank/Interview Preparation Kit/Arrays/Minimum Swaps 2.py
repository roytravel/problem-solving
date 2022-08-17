#!/bin/python3

import math
import os
import random
import re
import sys

def minimumSwaps(array):
    answer = 0
    for i in range(len(array)):
        while array[i] != i+1:
            temp = array[i]
            array[i] = array[temp-1]
            array[temp-1] = temp
            answer += 1
    return answer

if __name__ == '__main__':
    print(minimumSwaps([2,3,4,1,5]))