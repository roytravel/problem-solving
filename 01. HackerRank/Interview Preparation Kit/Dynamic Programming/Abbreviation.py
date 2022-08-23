def abbreviation(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m+1):
            if dp[i][j]:
                if j < m and a[i].upper() == b[j]:
                    dp[i+1][j+1] = 1
                if a[i].islower():
                    dp[i+1][j] = 1
    if dp[-1][-1]:
        return ("YES")
    else:
        return ("NO")


# Failed: 12/16, Success: 4/16
# def abbreviation(a, b):
#     remove = []
#     for char in a:
#         if char.islower() and char not in b and char.upper() not in b:
#             remove.append(char)
    
#     a = list(a)
#     for char in remove:
#         while char in a:
#             a.remove(char)

#     a = ''.join(a).upper()
    
#     for char in a:
#         if a.count(char) < b.count(char):
#             return "NO"

#     if a == b:
#         return "YES"
#     else:
#         return "NO"

# Failed: 12/16, Success: 4/16
# def abbreviation(a, b):
#     remove = []
#     for i in range(len(a)):
#         if a[i].lower() not in b.lower() and a[i] != a[i].upper():
#             remove.append(a[i])
    
#     a = list(a)
#     for i in remove:
#         a.remove(i)
    
#     a = ''.join(a)
#     a = a.upper()
#     if a == b:
#         return ("YES")
#     else:
#         return ("NO")
            

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        a = input()
        b = input()
        result = abbreviation(a, b)
        print (result)