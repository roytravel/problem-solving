from collections import defaultdict
string = "ifailuhkqq"

def sherlockAndAnagrams(s):
    total = 0
    dic = defaultdict(int)
    for i in range(1, len(s)):
        for j in range(len(s)-i+1):
            substring = ''.join(sorted(s[j:j+i]))
            total += dic[substring]
            dic[substring] += 1
    return total

print (sherlockAndAnagrams(string))