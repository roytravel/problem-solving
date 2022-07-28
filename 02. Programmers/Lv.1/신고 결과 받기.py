from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    user = defaultdict(set)
    count = defaultdict(int)
    
    for i in report:
        src, tgt = i.split()
        user[src].add(tgt)
        count[tgt] += 1
    
    for i in id_list:
        result = 0
        for j in user[i]:
            if count[j] >= k:
                result +=1
        answer.append(result)
    return answer