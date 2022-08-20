# I don't know why it occurr run-time error
# import sys
# input = sys.stdin.readline

# def quick_sort(array):
#     if len(array) <= 1:
#         return array

#     pivot = array[len(array)//2]
#     small, mid, big = [], [], []

#     for n in array:
#         if n < pivot:
#             small.append(n)
#         elif n > pivot:
#             big.append(n)
#         else:
#             mid.append(n)
    
#     return quick_sort(small) + mid + quick_sort(big)

# array = []
# N = int(input())
# for _ in range(N):
#     array.append(int(input()))

# arr = quick_sort(array)
# for i in arr:
#     print (i)