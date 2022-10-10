import math
L = int(input())

if L % 5 == 0:
    print (L // 5)
else:
    print(math.ceil(L / 5))