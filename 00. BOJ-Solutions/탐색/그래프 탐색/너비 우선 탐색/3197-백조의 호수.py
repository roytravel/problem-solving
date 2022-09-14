from sys import stdin
from collections import deque
input = stdin.readline

def find_swan(lake, queue):
    n_queue = deque()
    while queue:
        x, y  = queue.popleft()
        if x == swan[1][0] and y == swan[1][1]:
            return True, None
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<=nx<R and 0<=ny<C) and not visited[nx][ny]:
                if lake[nx][ny] == 'X':
                    n_queue.append([nx, ny])
                else:
                    queue.append([nx, ny])
                visited[nx][ny] = True
    return False, n_queue


def melt_ice(water, lake):
    n_water = deque()
    while water:
        x, y = water.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<R and 0<=ny<C:
                if lake[nx][ny] == 'X':
                    n_water.append([nx, ny])
                    lake[nx][ny] = '.'
    return n_water


if __name__ == "__main__":
    R, C = map(int, input().split())
    day = -1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False for _ in range(C)] for _ in range(R)]
    queue, water = deque(), deque()
    lake, swan = [], []

    for row in range(R):
        part_of_lake = list(input().rstrip())
        for col, obj in enumerate(part_of_lake):
            if obj == '.' or obj == 'L':
                water.append([row, col])
            if obj == 'L':
                swan.append([row, col])
        lake.append(part_of_lake)

    x, y = swan[0][0], swan[0][1]
    queue.append([x, y])
    visited[x][y] = True

    while True:
        day += 1
        flag, n_queue = find_swan(lake, queue)
        if flag:
            break
        water = melt_ice(water, lake)
        queue = n_queue
    print(day)