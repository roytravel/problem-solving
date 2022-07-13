import sys
input = sys.stdin.readline 

N = int(input())
K = int(input())
sensor = []
array = []
sensor = list(map(int, input().split()))

sensor.sort(reverse=True)
for i in range(N-1):
    array.append(sensor[i] - sensor[i+1])

array.sort()
value = 0
for i in range(N-K):
    value += array[i]
print (value)