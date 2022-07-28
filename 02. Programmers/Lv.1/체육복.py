def solution(n, lost, reserve):
    answer = 0
    
    if len(lost) == 0 and len(reserve) == 0: # 2. Best
        answer = n
        return answer
    
    if len(lost) == 0 and len(reserve) > 0: # 1. Best
        answer = n
        return answer
    
    if len(lost) > 0 and len(reserve) == 0: # 4. Worst
        answer = n - len(lost)
        return answer
    
    if len(lost) > 0 and len(reserve) > 0: # 3. Medium
        
        new_reserve = set(reserve) - set(lost)
        new_lost = set(lost) - set(reserve)
        
        for r in new_reserve:
            if (r-1) in new_lost:
                new_lost.remove(r-1)
                    
            elif (r+1) in new_lost:
                new_lost.remove(r+1)
            
        answer = n - len(new_lost)
        return answer