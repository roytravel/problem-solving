import sys
input = sys.stdin.readline
string = input().strip()
stack = []
answer = 0
SUM = 1
for i in range(len(string)):
    if string[i] == "[":
        stack.append(string[i])
        SUM *= 3
    
    elif string[i] == "(":
        stack.append(string[i])
        SUM *= 2
    
    elif string[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        
        if string[i-1] == "(":
            answer += SUM
        
        stack.pop()
        SUM //= 2

    elif string[i] == "]":
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if string[i-1] == "[":
            answer += SUM

        stack.pop()
        SUM //= 3

if stack:
    print(0)
else:
    print(answer)