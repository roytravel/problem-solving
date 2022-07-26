import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
file = defaultdict(int)
for _ in range(N):
    name, ext = input().rstrip().split('.')
    if file[ext]:
        file[ext] += 1
    else:
        file[ext] = 1

file = sorted(file.items())
for k, v in file:
    print (k, v)