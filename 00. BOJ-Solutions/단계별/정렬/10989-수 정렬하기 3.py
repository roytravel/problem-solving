import sys
input = sys.stdin.readline
N = int(input())
limit = 10001
numbers = [0] * limit

for _ in range(N):
    num = int(input())
    numbers[num] +=1

for i in range(len(numbers)):
    if i !=0:
        for _ in range(numbers[i]):
            print (i)