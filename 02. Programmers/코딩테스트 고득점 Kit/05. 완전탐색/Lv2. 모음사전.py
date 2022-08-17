from itertools import product

def solution(word):
    vowel = "AEIOU"
    vowel1 = list(vowel)
    vowel2 = ["".join(i) for i in product(vowel, repeat=2)]
    vowel3 = ["".join(i) for i in product(vowel, repeat=3)]
    vowel4 = ["".join(i) for i in product(vowel, repeat=4)]
    vowel5 = ["".join(i) for i in product(vowel, repeat=5)]
    vowels = vowel1 + vowel2 + vowel3 + vowel4 + vowel5
    vowels.sort()
    return vowels.index(word)+1


# def solution(word):
#     words = []
#     vowel = "AEIOU"
#     def dfs(length, string):
#         if length == 5:
#             return
#         for i in range(len(vowel)):
#             words.append(string + vowel[i])
#             dfs(length+1, string + vowel[i])
#     dfs(0, "")
#     return words.index(word)+1


# from itertools import product
# def solution(word):
#     words = []
#     for i in range(1, 5+1):
#         for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
#             words.append(''.join(c))
#     words.sort()
#     return words.index(word)+1

print(solution("I"))