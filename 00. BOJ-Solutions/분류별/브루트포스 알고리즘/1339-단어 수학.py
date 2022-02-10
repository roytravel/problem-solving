import sys
input = sys.stdin.readline
N = int(input())
alphabets = []
alpha_dict = {}

for _ in range(N):
    alphabets.append(input().rstrip())

for alphabet in alphabets:
    square_root = len(alphabet) - 1
    for char in alphabet:
        if char in alpha_dict:
            alpha_dict[char] += pow(10, square_root)
        else:
            alpha_dict[char] = pow(10, square_root)        
        square_root -= 1

alpha_dict = sorted(alpha_dict.values(), reverse=True)
result, _max = 0, 9
for i in alpha_dict:
    result += i * _max
    _max -= 1
print (result)