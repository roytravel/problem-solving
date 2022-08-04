from collections import deque

def solution(people, limit):
    boat, SUM = 0, 0
    people.sort(reverse=True)
    people = deque(people)
    while people:
        if people[0] + people[-1] <= limit:
            boat +=1
            people.popleft()
            if len(people) >= 1:
                people.pop()
        else:
            people.popleft()
            boat += 1
    return boat