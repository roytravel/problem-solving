from collections import deque

def bfs(n, computers, com, visited):
    visited[com] = True
    queue = deque([com])
    while queue:
        com = queue.popleft()
        visited[com] = True
        for conn in range(n):
            if conn != com and computers[com][conn] == 1:
                if visited[conn] == False:
                    queue.append(conn)

def dfs(n, computers, com, visited):  
    visited[com] = True
    for conn in range(n):
        if com != conn and computers[com][conn] == 1:
            if visited[conn] == False:
                dfs(n, computers, conn, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for com in range(n):
        if visited[com] == False:
            bfs(n, computers, com, visited)
            answer += 1
    return answer

n = 3
print(solution(n, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print(solution(n, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1