import sys
import math
input = sys.stdin.readline 

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

a, b = map(int, input().split())
if b > 10000000:
    b = 10000000
for num in range(a, b+1):
    if str(num) == str(num)[::-1]:
        if is_prime(num):
            print (num)
print(-1)