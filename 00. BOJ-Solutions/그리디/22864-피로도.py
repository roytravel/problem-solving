import sys
input = sys.stdin.readline 
A, B, C, M = map(int, input().split()) # 피로도 증가량 # 일 감소량 # 피로도 감소량 # 피로도 최대량
current = 0
work = 0
for _ in range(24):
    if A > M: # OK
        break
    if current + A <= M:
        current = current + A
        work += B
    else:
        current = current - C
        if current < 0:
            current = 0
print (work)