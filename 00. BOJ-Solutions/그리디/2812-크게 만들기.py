    import sys 
    input = sys.stdin.readline
    N, K = map(int, input().split())
    nums = list(map(int, input().strip()))
    stack = []
    count = K

    for i in range(N):
        while count > 0 and stack:
            if stack[-1] < nums[i]:
                stack.pop()
                count = count - 1
            else:
                break
        stack.append(nums[i])

    for i in range(N-K):
        print (stack[i], end="")