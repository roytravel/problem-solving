from itertools import combinations

# Solution 1
def pairs(k, arr):
    arr = set(arr)
    cnt = 0
    for i in arr:
        if i+k in arr:
            cnt += 1
    return cnt
    #return sum(1 for i in arr if i+k in arr)

# Solution 2 - Hash map
def pairs(k, arr):
    diff = {}
    res = 0
    for n in arr:
        diff[n] = 1
        if n+k in diff:
            res += 1
        if n-k in diff:
            res += 1
    return res

# Solution 3 - Two pointer
def pairs(k, arr):
    arr.sort()
    cnt = 0
    j = 1
    for i in range(n-1):
        while j < n:
            if arr[j] - arr[i] == k:
                cnt += 1
                j += 1
            elif arr[j] - arr[i] < k:
                j += 1
            elif arr[j] - arr[i] > k:
                break
    return cnt

# Time over 5/17, Success: 12/17
def pairs(k, arr):
    cnt = 0 
    for i in range(n):
        j = i + 1
        while j < n:
            if abs(arr[i]-arr[j]) == k:
                cnt += 1
            j += 1
    return cnt

# Time over 5/17, Success: 12/17
def pairs(k, arr):
    count = 0
    arr.sort(reverse=True)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]-arr[j] == k:
                count += 1
                break
    return count

# Time over 5/17, Success: 12/17
def pairs(k, arr):
    count = 0
    comb = combinations(arr, 2)
    for res in comb:
        if abs(res[0] - res[1]) == k:
            count += 1
    return count

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    print (result)
