import sys
input = sys.stdin.readline

N, M = map(int, input().split())
known = set(input().split()[1:])
party = []

for _ in range(M):
    party.append(set(input().split()[1:]))

print (party)

for _ in range(M):
    for p in party:
        if p & known:
            known = known.union(p)
        print (known)

count = 0
for p in party:
    print (p, known, count)
    if p & known:
        continue
    count += 1

print (count)


# Wrong
# N, M = map(int, input().split())
# truth = list(map(int, input().split()))

# if truth[0] != 0:
#     known = truth[1:]
# else:
#     known = [0]

# count = 0

# for _ in range(M):
#     party = list(map(int, input().split()))
#     people = party[1:]

#     for i in people:
#         if i in known:
#             break
#     else:
#         count += 1

# print(count)