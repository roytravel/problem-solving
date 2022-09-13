import sys
input = sys.stdin.readline

bar = input().rstrip()
stack = []
count = 0

for i in range(len(bar)):
    if bar[i] == "(":
        stack.append(bar[i])
    
    elif bar[i] == ")":
        if bar[i-1] == ")":
            count += 1
            stack.pop()
        else:
            stack.pop()
            count += len(stack)

print (count)