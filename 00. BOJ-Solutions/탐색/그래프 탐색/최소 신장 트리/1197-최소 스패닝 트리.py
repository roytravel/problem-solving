import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())
graph = []
for _ in range(E):
    a, b, cost = map(int, input().split())
    graph.append([a, b, cost])

graph.sort(key=lambda x:x[2])

parent = [0] * (V+1)
for i in range(1, V+1):
    parent[i] = i

costs = 0
for i in range(E):
    a, b, cost = graph[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        costs += cost

print (costs)