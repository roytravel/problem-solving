def solution(s):
    answer = True
    stack = [0]
    
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")" and stack[-1] == "(":
            stack.pop()
        else:
            return False
        
    if stack[0] == 0 and len(stack) == 1:
        return True
    else:
        return False