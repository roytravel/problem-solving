def dfs(graph, node, visited):
    if visited[node]:
        return 0

    visited[node] = True
    count = 1
    for neighbor in graph[node]:
        count += dfs(graph, neighbor, visited)
    return count


def roadsAndLibraries(n, c_lib, c_road, cities):
    cost = 0

    # 1. make graph
    graph = {i: [] for i in range(1, n+1)}
    for u, v in cities:
        graph[u].append(v)
        graph[v].append(u)

    # 2. traverse graph using graph
    visited = [0] * (n+1)
    for node in graph:
        count = dfs(graph, node, visited)
        if count:
            cost += c_lib + ((count-1) * min(c_lib, c_road))
    return cost


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        c_lib = int(first_multiple_input[2])
        c_road = int(first_multiple_input[3])
        cities = []
        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))
        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print (result)