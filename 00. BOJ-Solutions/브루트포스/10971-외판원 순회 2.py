import sys
import copy

def get_cases_of_travel_city() -> None:
    if len(path) == N:
        all_paths.append(copy.deepcopy(path))
        return

    for i in range(N):
        if i not in path:
            path.append(i)
            get_cases_of_travel_city()
            path.pop()


def get_min_path_cost(all_paths: list) -> int:
    cost = sys.maxsize
    for path in all_paths:
        result = 0
        for x in range(len(path)-1):
            if x == len(path) -2:
                result += cost_matrix[path[x+1]][path[0]]
            result += cost_matrix[path[x]][path[x+1]]
        cost = min(result, cost)
    return cost

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    cost_matrix = []
    visited = [0] * N
    path = []
    all_paths = []

    for _ in range(N):
        cost_matrix.append(list(map(int, input().split())))

    get_cases_of_travel_city()
    cost = get_min_path_cost(all_paths)
    print (cost)