import os
from collections import defaultdict

def isBalanced(s):
    # partially correct: there is corner case
    # if len(s) % 2 != 0:
    #     return "NO"
    
    # dictionary = defaultdict(str)
    # dictionary['{'] = "}"
    # dictionary['['] = "]"
    # dictionary['('] = ")"
    # #dictionary = {'{':'}', '[':']', '(':')'}
    # s = list(s)
    # for i in range(len(s)//2):
    #     start = s[i]
    #     end = s.pop()
    #     if dictionary[start] == end:
    #         continue
    #     else:
    #         return "NO"
    # return "YES"

    # partially correct (3/21): Runtime error
    # stack = []
    # pairs = ["{}", "[]", "()"]
    # for i in s:
    #     if i in ["{", "[", "("]:
    #         stack.append(i) 
    #     else:
    #         front = stack.pop() 
    #         back = i
    #         if front + back in pairs:
    #             continue
    #         else:
    #             return "NO"
    # return "YES"

    # partially correct (18/21): Wrong Answer
    # stack = []
    # pairs = ["{}", "[]", "()"]
    # for i in s:
    #     if i in ["{", "[", "("]:
    #         stack.append(i) 
    #     else:
    #         if not stack:
    #             return "NO"
    #         front = stack.pop() 
    #         back = i
    #         if front + back in pairs:
    #             continue
    #         else:
    #             return "NO"      
    # return "YES"

    # solution
    stack = []
    pairs = ["{}", "[]", "()"]
    for i in s:
        if i in ["{", "[", "("]:
            stack.append(i) 
        else:
            if not stack:
                return "NO"
            front = stack.pop() 
            back = i
            if front + back in pairs:
                continue
            else:
                return "NO"
    if stack:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        fptr.write(result + '\n')
    fptr.close()