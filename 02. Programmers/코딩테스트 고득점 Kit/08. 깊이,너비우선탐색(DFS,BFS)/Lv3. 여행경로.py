from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    answer = []
    for src, dst in tickets:
        graph[src].append(dst)
    
    for src, dst in graph.items():
        graph[src].sort(reverse=True)

    stack = ['ICN']
    while stack:
        src = stack[-1]
        if not graph[src]:
            answer.append(stack.pop())
        else:
            stack.append(graph[src].pop())
    answer.reverse()
    return answer


# from collections import defaultdict

# answer = []
# graph = defaultdict(list)

# def dfs(src):
#     while graph[src]:
#         dfs(graph[src].pop(0))
        
#     if not graph[src]:
#         answer.append(src)
#         return

# def solution(tickets):    
#     for src, dst in tickets:
#         graph[src].append(dst)
    
#     for k, v in graph.items():
#         graph[k].sort()
        
#     dfs("ICN")
#     return answer[::-1]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
#print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))