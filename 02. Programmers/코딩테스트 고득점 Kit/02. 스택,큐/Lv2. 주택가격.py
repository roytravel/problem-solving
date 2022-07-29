from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        x = prices.popleft()
        sec = 0
        for i in prices:
            sec += 1
            if x > i:
                break
        answer.append(sec)
    return answer