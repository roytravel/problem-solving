# This problem asked to people that do you know union-find algorithm?
import sys
input = sys.stdin.readline

answer = 0
people, party = map(int, input().split())
known = set(input().split()[1:])
participant = []

for _ in range(party):
    participant.append(set(input().split()[1:]))

for _ in range(party):
    for p in participant:
        if p & known:
            known = known.union(p)
    
for p in participant:
    if p & known:
        continue
    answer += 1
print (answer)