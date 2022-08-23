# Soltuion
def stepPerms(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2 
    elif n == 3:
        return 4 
    
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        
    return dp[n]

# Time limit: 4/11, Success: 7/11
def stepPerms(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    return stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)


if __name__ == '__main__':
    s = int(input().strip())
    for s_itr in range(s):
        n = int(input().strip())
        res = stepPerms(n)
        print (res)