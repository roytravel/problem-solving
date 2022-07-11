import sys
input = sys.stdin.readline
while True:
    cipher = input().rstrip()
    if cipher == "END":
        break
    print(cipher[::-1])