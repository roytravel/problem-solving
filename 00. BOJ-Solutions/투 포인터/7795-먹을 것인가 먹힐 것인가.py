import sys
input = sys.stdin.readline

def binary_search(brray, a):
    start, end = 0, len(brray)-1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if brray[mid] < a:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    brray = list(map(int, input().split()))
    array.sort()
    brray.sort()
    count = 0
    for a in array:
        count += binary_search(brray, a) + 1
    print(count)


# import sys
# input = sys.stdin.readline
# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     array = list(map(int, input().split()))
#     brray = list(map(int, input().split()))

#     array.sort()
#     brray.sort()
#     count, pair = 0, 0
    
#     for i in range(N):
#         while True:
#             if count == M or array[i] <= brray[count]:
#                 pair += count
#                 break
#             else:
#                 count += 1
#     print (pair)

# Time over
# import sys
# input = sys.stdin.readline
# T = int(input())
# for _ in range(T):
#     A, B = map(int, input().split())
#     array = list(map(int, input().split()))
#     brray = list(map(int, input().split()))
#     count = 0
#     for a in array:
#         for b in brray:
#             if a > b:
#                 count += 1
#     print(count)