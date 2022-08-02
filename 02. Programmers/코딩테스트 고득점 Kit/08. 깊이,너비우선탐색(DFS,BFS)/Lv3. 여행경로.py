from collections import defaultdict

answer = []
graph = defaultdict(list)

def dfs(src):
    while graph[src]:
        dfs(graph[src].pop(0))
        
    if not graph[src]:
        answer.append(src)
        return

def solution(tickets):    
    for src, dst in tickets:
        graph[src].append(dst)
    
    for k, v in graph.items():
        graph[k].sort()
        
    dfs("ICN")
    return answer[::-1]