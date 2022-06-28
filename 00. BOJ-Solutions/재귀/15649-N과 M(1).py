from itertools import permutations

def recursion():
    if len(picked) == M:
        print (' '.join(str(i) for i in picked))
        return
    
    for i in range(1, N+1):
        if i not in picked:
            picked.append(i)
            recursion()
            picked.pop()
            
def dfs(depth) -> None:
    if depth == M:
        print (*picked)
        return
    
    for i in range(N):
        if not visited[i]: # 방문하지 않았으면
            visited[i] = True # 방문했다고 체크하고
            picked.append(i+1) # 값 수집하고
            dfs(depth+1) # 재귀를 통해 
            visited[i] = False
            picked.pop()
    

if __name__ == "__main__":
    
    N, M = list(map(int, input().split()))
    
    # method 1. use permutations function in itertools library.
    # array = [i+1 for i in range(N)]
    # result = list(permutations(array, M))
    # for i in result:
    #     print (*i)

    # method 2. use Recursion
    # picked = []
    # recursion()

    # method 3. use DFS (Depth First Search)
    visited = [False] * N
    picked = []
    dfs(0)