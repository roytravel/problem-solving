from collections import defaultdict
num = defaultdict(int)

N = int(input())
array1 = list(map(int, input().split()))
M = int(input())
array2 = list(map(int, input().split()))

for n in array1:
    num[n] += 1

for n in array2:
    if num[n]:
        print (1)
    else:
        print (0)