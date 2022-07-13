import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

class dictionary:
    def __init__(self, item) -> None:
        self.item = item
    
    def __str__(self):
        return self.item

    def __repr__(self):
        return "'"+self.item+"'"


directory = {}

for _ in range(N+M):
    P, F, C = list(input().split())
    directory[dictionary(P)] = F

#print (directory["main"])
print (type(directory))
for i,v in directory:
    print (i, v)
# for k, v in directory:
#     print (k, v)


# Q = int(input())
# for _ in range(Q):
#     query = input()
#     print (something)