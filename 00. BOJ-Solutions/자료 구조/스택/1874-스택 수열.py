N = int(input())
stack = []
result = []
flag = 0
now = 1
for i in range(N):
    num = int(input())
    while now <= num:
        stack.append(now)
        result.append("+")
        now += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        flag = 1
        break      

if flag == 0:
    for i in result:
        print(i)

# 100%가 보였지만 틀림
# import sys
# input = sys.stdin.readline

# N = int(input())
# stack = []
# for _ in range(N):
#     stack.append(int(input()))

# now = 0
# result = []
# array = [0]
# i = 1
# flag = True
# while array:
#     if stack[now] == array[-1]:
#         array.pop()
#         result.append("-")
#         now += 1
#     else:
#         result.append("+")
#         array.append(i)
#         i = i + 1

#     if len(array) > N:
#         print ("NO")
#         flag = False
#         break

#     elif array[0] == 0 and len(array) == 1 and now == N:
#         break

# if flag:
#     for i in result:
#         print (i)