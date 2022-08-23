from collections import defaultdict, deque


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = defaultdict(list)
    color = defaultdict(int)
    
    # 1. make graph with given from-to information
    for f, t in zip(graph_from, graph_to):
        graph[f].append(t)
        graph[t].append(f)
        
        # 2. make color information
        if f not in color:
            color[f] = ids[f-1]
        if t not in color:
            color[t] = ids[t-1]
    
    # 3. traverse node using bfs
    queue = deque()
    queue.append([val, 0])
    start_color = color[val]
    visited = set()
    while queue:
        current, count = queue.popleft()
        visited.add(current)
        for x in graph[current]:
            if x not in visited:
                if color[x] == start_color:
                    return count+1
                visited.add(x)
                queue.append([x, count+1])
    return -1


if __name__ == '__main__':
    graph_nodes, graph_edges = map(int, input().split())
    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))
    val = int(input())
    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)
    print (ans)