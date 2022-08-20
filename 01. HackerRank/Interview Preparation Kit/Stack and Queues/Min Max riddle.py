def riddle(arr):
    i = 0
    stack = []
    result = [0] * n
    while i < n or stack:
        if not stack or (i < n and arr[stack[-1]] <= arr[i]):
            stack.append(i)
            i += 1
            continue

        top = stack.pop()
        if stack:
            idx = i - stack[-1]-1 - 1
        else:
            idx = i - 1

        result[idx] = max(result[idx], arr[top])
    
    for i in range(n-2, -1, -1):
        if result[i] == 0 or result[i+1] > result[i]:
            result[i] = result[i+1]
            
    return result

# Time over 3/8, Success: 5/8
def riddle(arr):
    answer = []
    for w in range(1, n+1):
        nums = []
        for i in range(n-w+1):
            nums.append(min(arr[i:i+w]))
        answer.append(max(nums))
    return answer

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = riddle(arr)
    for i in res:
        print (i, end=' ')
