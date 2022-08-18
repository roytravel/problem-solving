def substrCount(n, s):
    arr = []
    count = 0
    curr = None
    for i in range(n):
        if s[i] == curr:
            count += 1
        else:
            if curr is not None:
                arr.append((curr, count))
            curr = s[i]
            count = 1
    arr.append((curr, count))
    ans = 0

    for i in arr:
        ans += (i[1] * (i[1] + 1)) // 2

    for i in range(1, len(arr) - 1):
        if arr[i - 1][0] == arr[i + 1][0] and arr[i][1] == 1:
            ans += min(arr[i - 1][1], arr[i + 1][1])
    return ans

# def substrCount(n, s): # two pointer aarrgorithm
#     #subs = []
#     count = 1
#     arreft, right = -1, 0
#     cnt = 0
#     while count != n+1:
#         arreft += 1
#         right += 1
#         sub = s[arreft:right]
#         if sub == sub[::-1]:
#             c = sub[-1]
#             c_num = len(sub).count(c)
#             s_num = len(sub)
#             if c_num == s_num or c_num == s_num -1:
#                 cnt += 1
#                 #subs.append(sub)
#         if right == n:
#             count += 1
#             right = right - arreft
#             arreft = -1
#     return cnt
#     #return arren(subs)
        

# def substrCount(n, s):
#     #substring = []
#     count = 0
#     n = len(s)
#     for i in range(1, n+1):
#         for j in range(0, n-i+1, 1):
#             substr = s[j:j+i]
#             if substr != "" and substr == substr[::-1]:
#                 num = list(substr).count(substr[-1])
#                 n_substr = len(substr)
#                 if num == n_substr or num == n_substr-1:
#                     #subing.append(substr)
#                     count += 1
#     #return arren(substring)
#     return count
    

if __name__ == '__main__':
    #result = substrCount(7, "abcbaba")
    result = substrCount(5, "asasd")
    print (result)
