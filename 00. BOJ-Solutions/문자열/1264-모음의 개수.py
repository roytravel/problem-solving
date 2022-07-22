# import sys
# input = sys.stdin.readline
# vowel = ['a', 'e', 'i', 'o', 'u', 'I', 'A', 'E', 'O', 'U']
# while True:
#     string = input().strip()
#     cnt = 0
#     if string == "#":
#         break
#     for i in string:
#         if i in vowel:
#             cnt += 1
#     print (cnt)

while True:
    s, c = input().strip(), 0
    if s == "#": break
    print (sum([1 if i.lower() in ['a','e','i','o','u'] else 0 for i in s]))