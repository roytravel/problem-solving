def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        string = s[:i]
        count = 1
        result = ""
        for j in range(i, len(s)+i, i):
            if string == s[j:j+i]:
                count += 1
            else:
                if count == 1:
                    result += string
                else:
                    result += str(count)+string
                string = s[j:j+i]
                count = 1
        answer = min(answer, len(result))
    return answer 

example = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]
for i in example:
    print(solution(i))