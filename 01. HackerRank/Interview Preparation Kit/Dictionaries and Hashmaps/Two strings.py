import os

def twoStrings(s1, s2):    
    # solution 1
    # s1 = set(list(s1))
    # s2 = set(list(s2))
    # intersection = s1.intersection(s2)
    # if len(intersection) != 0:
    #     return "YES"
    # return "NO"

    # solution 2
    s1 = set(s1)
    s2 = set(s2)
    if s1 & s2 != set():
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)
        fptr.write(result + '\n')
    fptr.close()