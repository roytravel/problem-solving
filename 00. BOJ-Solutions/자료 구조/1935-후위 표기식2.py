N = int(input())
post_expression = input()
nums = [int(input()) for _ in range(N)]
stack = []
items = dict()

for i in post_expression:
    if i in "*/+-":
        a = stack.pop()
        b = stack.pop()
        if i == "*":
            stack.append(b*a)
        elif i == "/":
            stack.append(b/a)
        elif i == "+":
            stack.append(b+a)
        elif i == "-":
            stack.append(b-a)
    else:
        stack.append(nums[ord(i)-ord('A')])

print (format(stack[0], ".2f"))