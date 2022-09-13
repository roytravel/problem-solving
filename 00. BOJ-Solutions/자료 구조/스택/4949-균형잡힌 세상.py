import sys
input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    stack = []
    if sentence == '.':
        break
    
    for s in sentence:
        if s == "(" or s == "[":
            stack.append(s)

        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(')')
                break
        
        elif s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(']')
                break

    if not stack:
        print ("yes")
    else:
        print ("no")