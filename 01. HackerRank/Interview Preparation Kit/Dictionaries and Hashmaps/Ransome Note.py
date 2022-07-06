import sys
from collections import Counter

def checkMagazine(magazine, note):
    # solution 1 
    for word in note:
        if word not in magazine:
            print ("No")
            exit()
        else:
            magazine.remove(word)
    print ("Yes")

    # solution 2
    if Counter(note) - Counter(magazine) == {}:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    input = sys.stdin.readline
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    checkMagazine(magazine, note)