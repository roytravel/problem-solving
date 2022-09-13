import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    array = deque(list(map(int, input().split())))
    checklist = [0 for _ in range(N)]
    checklist[M] = True
    count = 0
    while True:
        if array[0] == max(array):
            count +=1
            if checklist[0]:
                del array[0]
                del checklist[0]
            else:
                print(count)
                break
        else:
            array.append(array[0])
            checklist.append(checklist[0])
            del array[0]
            del checklist[0]

# 왜 틀렸지
# import sys
# from collections import deque
# input = sys.stdin.readline

# T = int(input())
# for i in range(T):
#     N, M = map(int, input().split())
#     priority = 0
#     array = deque(map(int, input().split()))
#     target = array[M]
#     flag = False
#     while array:
#         if array[0] != max(array):
#             array.append(array.popleft())
#         else:
#             value = array.popleft()
#             if target == value:
#                 priority += 1
#                 if array.count(value) == 0:
#                     break
#                 else:
#                     flag = True
#             else:
#                 priority += 1

#     if flag:
#         print (priority - 1)
#     else:
#         print (priority)