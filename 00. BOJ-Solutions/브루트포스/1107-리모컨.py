# Solve it again.
import sys
input = sys.stdin.readline

target = int(input())
M = int(input())
answer = abs(100 - target)
broken = set(input().split()) if M else set()

for num in range(1_000_001):
    for n in str(num):
        if n in broken:
            break
    else:
        answer = min(answer, len(str(num)) + abs(num-target))
print (answer)