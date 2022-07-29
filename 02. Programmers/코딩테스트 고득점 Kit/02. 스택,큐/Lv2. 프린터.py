from collections import deque

def solution(priorities, location):
    printer = deque()
    for idx, priority in enumerate(priorities):
        printer.append((idx, priority))
        
    count = 0
    while printer:
        current = printer.popleft()
        if all(current[1] >= q[1] for q in printer):
            count += 1
            if current[0] == location:
                answer = count
                return answer
        else:
            printer.append(current)