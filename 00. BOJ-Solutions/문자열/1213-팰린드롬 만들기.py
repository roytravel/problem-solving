import sys
from collections import Counter
input = sys.stdin.readline
name = list(map(str, input().strip()))
name.sort()
counter = Counter(name)
count = 0
center = ""

for i in counter:
    if counter[i] % 2 != 0:
        count += 1
        center += i
        name.remove(i)
    if count > 1:
        break

if count > 1:
    print ("I'm Sorry Hansoo")
else:
    result = ""
    for i in range(0, len(name), 2):
        result += name[i]
    print(result + center + result[::-1])