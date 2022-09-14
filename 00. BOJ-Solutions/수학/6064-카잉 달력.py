def calendar(M, N, x, y):
    while x <= M * N:
        if (x-y) % N == 0:
            return x
        x += M
    return -1

T = int(input())
for i in range(T):
    M, N, x, y = map(int, input().split())
    print(calendar(M, N, x, y))


# Time over 2
# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     M, N, a, b = map(int, input().split())
#     X, Y = 1, 1
#     count = M * N
#     index = 1
#     while count != index:
#         index += 1
#         x, y = X, Y

#         if x < M:
#             x += 1
#         else:
#             x = 1
        
#         if y < N:
#             y += 1
#         else:
#             y = 1

#         X, Y = x, y 
#         if (X, Y) == (a, b):
#             print (index)
#             break
#     else:
#         print (-1)

# time over
# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     M, N, a, b = map(int, input().split())
#     array = [[1, 1]]
#     count = M * N
#     temp = 1
#     while count != temp:
#         x, y = array[-1][0], array[-1][1]
#         if x < M:
#             x += 1
#         else:
#             x = 1
        
#         if y < N:
#             y += 1
#         else:
#             y = 1

#         array = [[x, y]]
#         if (x, y) == (a, b):
#             print (temp+1)
#             break
#         temp += 1
#     else:
#         print (-1)


# memory over
# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     M, N, a, b = map(int, input().split())
#     array = [[1, 1]]
#     count = M * N
#     while count:
#         x = array[-1][0]
#         y = array[-1][1]

#         if x < M:
#             x += 1
#         else:
#             x = 1
        
#         if y < N:
#             y += 1
#         else:
#             y = 1

#         array.append([x, y])
#         count -= 1
    
#     if [a, b] in array:
#         print (array.index([a, b])+1)
#     else:
#         print (-1)