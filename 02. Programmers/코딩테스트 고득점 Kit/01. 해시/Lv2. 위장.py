from collections import defaultdict
    
def solution(clothes):
    clothe = defaultdict(int)
    for i in clothes:
        name, _type = i[0], i[1]
        clothe[_type] += 1
        
    n = 1
    for i in clothe.values():
        n = n * (i+1)

    return n-1