"""
ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd
[111, 111, 111, 111, 111, 111, 111, 111, 111, 1]
1 111
YES, but my answer is NO

aaaaabc
[5, 1, 1]
1 5
NO, but my answer is YES
"""

# Success
from collections import defaultdict

def isValid(s):
    dic = defaultdict(int)
    for c in s:
        dic[c] += 1
        
    arr = list(dic.values())
    n = len(arr)
    MIN, MAX = min(arr), max(arr)
    
    if MIN == MAX:
        return "YES"
    elif arr.count(MAX) == 1 and n - arr.count(MIN) == 1 and MAX-MIN == 1:
        return "YES"
    elif arr.count(MIN) == 1 and n - arr.count(MAX) == 1:
        return "YES"
    else:
        return "NO"


# Wrong answer fail: 2/20, success: 18/20
# def isValid(s):
#     dic = defaultdict(int)
#     for c in s:
#         dic[c] += 1
    
#     arr = list(dic.values())
#     print (arr)
#     MIN, MAX = min(arr), max(arr)
#     print (MIN, MAX)
    
#     if MIN == MAX:
#         return "YES"
    
#     elif arr.count(MAX) == 1 and arr.count(MIN) == len(arr)-1:
#         return "YES"
    
#     elif arr.count(MIN) == 1 and arr.count(MAX) == len(arr)-1:
#         return "YES"
    
#     else:
#         return "NO"


# Wrong answer fail: 2/20, success: 18/20
# def isValid(s):
#     dic = defaultdict(int)
#     for c in s:
#         dic[c] += 1
        
#     arr = list(dic.values())
#     MIN = min(arr)
#     MAX = max(arr)
    
#     if MIN == MAX:
#         return "YES"
    
#     elif MAX > MIN and arr.count(MAX) == 1 and arr.count(MIN) == len(arr)-1:
#         return "YES"
    
#     elif MAX > MIN and arr.count(MIN) == 1 and arr.count(MAX) == len(arr)-1:
#         return "YES"
    
#     else:
#         return "NO"


# Wrong answer fail: 9/20, success: 11/20
# def isValid(s):
#     dic = defaultdict(int)
#     for c in s:
#         dic[c] += 1
        
#     arr = list(dic.values())
#     MIN = min(arr)
#     MAX = max(arr)
    
#     if MIN == MAX:
#         return "YES"
    
#     elif MAX > MIN and arr.count(MAX) == 1:
#         return "YES"
    
#     elif MAX > MIN and arr.count(MIN) == 1:
#         return "YES"
    
#     else:
#         return "NO"
        

if __name__ == '__main__':
    s = input()
    result = isValid(s)
    print (result)
