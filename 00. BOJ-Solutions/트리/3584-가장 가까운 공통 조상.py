import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    parent = [0] * (N+1)
    for __ in range(N-1):
        A, B = map(int, input().split())
        parent[B] = A
    
    n1, n2 = map(int, input().split())
    target_n1 = [n1]
    target_n2 = [n2]
    while parent[n1]:
        target_n1.append(parent[n1])
        n1 = parent[n1]
    
    while parent[n2]:
        target_n2.append(parent[n2])
        n2 = parent[n2]

    target_n1_depth = len(target_n1) - 1
    target_n2_depth = len(target_n2) - 1

    while target_n1[target_n1_depth] == target_n2[target_n2_depth]:
        target_n1_depth -= 1
        target_n2_depth -= 1
    
    print (target_n1[target_n1_depth + 1])