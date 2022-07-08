import sys
input = sys.stdin.readline

def dfs(K: int) -> None:
    tree[K] = -2
    for i in range(N):
        if K == tree[i]:
            dfs(i)

if __name__ == "__main__":
    # input 
    N = int(input())
    tree = list(map(int, input().split()))
    K = int(input())

    # main algorithm
    dfs(K)

    # output
    count = 0 
    for i in range(len(tree)):
        if tree[i] != -2 and i not in tree: # 제거 표시인 -2도 아니고, 자신을 부모 노드로 갖는 노드도 존재하지 않을 경우
            count +=1
    print(count)