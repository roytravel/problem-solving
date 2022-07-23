import sys
from copy import deepcopy
input = sys.stdin.readline
numbers = list(map(int, input().split()))
numbers_asc = deepcopy(numbers)
numbers_asc.sort()
numbers_dsc = deepcopy(numbers)
numbers_dsc.sort(reverse=True)
if numbers == numbers_asc:
    print ("ascending")
elif numbers == numbers_dsc:
    print ("descending")
else:
    print ("mixed")