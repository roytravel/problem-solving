import sys
input = sys.stdin.readline
N = int(input())

count_re = 0
def fibonacci_re(n):
    global count_re
    count_re += 1
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_re(n-1) + fibonacci_re(n-2)
        
dp = [0, 1, 1]
def fibonaaci_dp(n):
    dp[1] = 1
    dp[2] = 1
    count_dp = 0
    for i in range(3, n+1):
        count_dp += 1
        dp.append(dp[i-1] + dp[i-2])
    return count_dp

print (fibonacci_re(N), fibonaaci_dp(N))