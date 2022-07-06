import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
stack = [-sys.maxsize]

for i in A:
    if stack[-1] < i:
        print (True, i)
        stack.append(i)
    else:
        print (False, i)
        stack[bisect_left(stack, i)] = i

print (stack)
print (len(stack)-1)

# solution 2
# import sys
# from bisect import bisect_left
# input = sys.stdin.readline

# N = int(input())
# A = list(map(int, input().split()))
# stack = [sys.maxsize]

# for i in A:
#     if stack[-1] < i:
#         stack.append(i)
#     else:
#         stack[bisect_left(stack, i)] = i

# print (len(stack))