import sys
input = sys.stdin.readline

string = input().strip()
alphabet = ['U', 'C', 'P', 'C']
answer = ""
count = 0
for a in alphabet:
    if a in string:
        answer += a
        string = string[string.index(a)+1:]
    else:
        print("I hate UCPC")
        break

if answer == "UCPC":
    print("I love UCPC")

# Wrong
# import sys
# input = sys.stdin.readline
# string = input().strip()
# string = string.split()
# stack = []
# for s in string:
#     if "U" not in stack and "U" in s:
#         stack.append(s)
#     if "C" not in stack and "C" in s:
#         stack.append(s)
#     if "P" not in stack and "P" in s:
#         stack.append(s)
#     if "C" in stack and "C" in s:
#         stack.append(s)
# answer = ""
# for i in stack:
#     answer += i[0]

# if answer == "UCPC":
#     print("I love UCPC")
# else:
#     print("I hate UCPC")