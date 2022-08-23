def commonChild(s1, s2):

    n = len(s1)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[n][n]


# Wrong 11/15, Success 4/15
# from collections import defaultdict
# def commonChild(s1, s2):
#     count = 0
#     dic = defaultdict(int)    
#     for i in s2:
#         dic[i] += 1
    
#     for i in s1:
#         if dic[i] != 0:
#             dic[i] -= 1
#             count += 1
#     return count

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
    print (result)