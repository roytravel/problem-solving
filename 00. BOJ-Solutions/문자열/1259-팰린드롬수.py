import sys
input = sys.stdin.readline
while True:
    num = input().rstrip('\n')
    if num == '0':
        break

    if num == num[::-1]:
        print ("yes")
    else:
        print ("no")