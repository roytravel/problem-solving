import sys
input = sys.stdin.readline

N = int(input())
array = []
for i in range(N):
    array.append(int(input()))

count = 0
prior =  array[-1]
for i in range(len(array)-2, -1, -1):
    num = array[i]
    while num >= prior:
        num -= 1
        count += 1
    prior = num

print (count)