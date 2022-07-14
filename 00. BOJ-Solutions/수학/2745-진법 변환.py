import sys
input = sys.stdin.readline

N, B = input().split()

# dict = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15, "G":16, "H":17, "I":18, 
#         "J":19, "K":20, "L":21, "M":22, "N":23, "O":24, "P":25, "Q":26, "R":27, 
#         "S":28, "T":29, "U":30, "V":31, "W":32, "X":33, "Y":34, "Z":35}

# def translate_notion(N, B):
#     num = 0
#     length = len(N) -1
#     for char in str(N):
#         num += dict[char] * pow(B, length)
#         length = length -1
#     print (num)

# translate_notion(N, int(B))

print (int(N, int(B)))