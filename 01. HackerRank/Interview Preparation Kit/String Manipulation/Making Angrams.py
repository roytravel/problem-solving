import os
from collections import defaultdict

def makeAnagram(a, b):
    dictionary = defaultdict(int)
    for char in a:
        dictionary[char] += 1

    for char in b:
        dictionary[char] -= 1

    _sum = 0
    for key, value in dictionary.items():
        _sum += abs(value)

    return _sum        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = input()
    b = input()
    res = makeAnagram(a, b)
    fptr.write(str(res) + '\n')
    fptr.close()