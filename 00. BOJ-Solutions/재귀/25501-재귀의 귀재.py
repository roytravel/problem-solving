def recursion(s, l, r):
    if l >= r: 
        return 1
    elif s[l] != s[r]: 
        return 0
    else:
        global count
        count += 1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    global count
    count += 1
    return recursion(s, 0, len(s)-1)


N = int(input())
for _ in range(N):
    count = 0
    string = input().strip()
    print(isPalindrome(string), count)