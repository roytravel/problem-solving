import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()
length = sum(array)
answer = 0

for num in array:
    answer += num * (length - num)
    length -= num

print (answer)