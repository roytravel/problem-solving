def solution(answers):
    answer = []
    length = len(answers)
    s1, s2, s3 = 0, 0, 0
    n1, n2, n3 = 2, 2, 2
    method1 = [1, 2, 3, 4, 5] # 5
    method2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    method3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    
    while True:
        if len(method1) < length:
            method1 = method1 * n1
            n1 += 1
        elif len(method2) < length:
            method2 = method2 * n2
            n2 += 1
        elif len(method3) < length:
            method3 = method3 * n3
            n3 += 1
        else:
            break
    
    for i in range(len(answers)):
        if answers[i] == method1[i]:
            s1 += 1
        if answers[i] == method2[i]:
            s2 += 1
        if answers[i] == method3[i]:
            s3 += 1
    
    MAX = max(s1, s2, s3)
    if MAX == s1:
        answer.append(1)
    if MAX == s2:
        answer.append(2)
    if MAX == s3:
        answer.append(3)
    
    return answer