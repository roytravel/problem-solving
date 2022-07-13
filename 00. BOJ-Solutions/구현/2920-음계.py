import sys
input = sys.stdin.readline
nums = list(map(int, input().split()))

if nums[0] == 1:
    for i in range(1, 9):
        if nums[i-1] != i:
            print ("mixed")
            break
    else:
        print ("ascending")

if nums[0] == 8:
    for i in range(8, 0, -1):
        if nums[8-i] != i:
            print ("mixed")
            break
    else:
        print ("descending")