import os

def repeatedString(s, n):
    if "a" not in s:
        return 0
    elif len(s) == 1 and s[0] == "a":
        return n 
    else:
        q, r = divmod(n, len(s))
        frequency = q * s.count('a') + s[:r].count('a')
        return frequency
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input().strip())
    result = repeatedString(s, n)
    fptr.write(str(result) + '\n')
    fptr.close()