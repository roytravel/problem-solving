import sys
input = sys.stdin.readline

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[j] > array[i]:
                array[j], array[i] = array[i], array[j]
    return array

array = []
N = int(input())
for _ in range(N):
    array.append(int(input()))

arr = bubble_sort(array)
for i in arr:
    print (i)