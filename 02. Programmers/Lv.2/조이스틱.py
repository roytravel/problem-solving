def solution(name):
    answer = 0
    next_idx = 0
    min_l_r = len(name)
    for i, char in enumerate(name):
        # A에 가까운지 Z에 가까운지를 판단하여 상하 조작 횟수 최소값 구하기 
        answer += min(ord(char) - ord("A"), ord("Z") - ord(char) +1)
        
        # 오른쪽으로 가는 것과 오른쪽으로 갔다 왼쪽으로 가는 것 두 개다 구해서 최소 값을 판단하여 좌우 조작 횟수 최소값 구하기
        next_idx = i + 1
        while next_idx < len(name) and name[next_idx] == "A":
            next_idx += 1
        
        backward = i + i + len(name) - next_idx
        min_l_r = min(min_l_r, backward)
            
    answer += min_l_r
    return answer