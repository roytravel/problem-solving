import sys
input = sys.stdin.readline

string = input().strip()
bomb = input().strip()
stack = []

for i in range(len(string)):
    stack.append(string[i])
    if string[i] == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]
answer = ''.join(stack)

if not answer:
    print("FRULA")
else:
    print (answer)

    

# Time over
# import sys
# input = sys.stdin.readline
# str1 = input().strip()
# str2 = input().strip()
# flag = True
# while flag:
#     before = str1
#     str1 = str1.replace(str2, '')
#     if before == str1:
#         flag = False

#     if not str1:
#         print("FRULA")
#         exit()
# print (str1)