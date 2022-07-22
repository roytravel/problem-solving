# short coding 1
[print("yes") if 6 <= len(input().strip()) <= 9 else print("no") for _ in range(int(input()))]

# short coding 2
for _ in range(int(input())):
    print ("yes" if 6 <= len(input().strip()) <= 9 else "no")

# short coding 3
import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    password = input().strip()
    if 6 <= len(password) <= 9:
        print ("yes")
    else:
        print ("no")