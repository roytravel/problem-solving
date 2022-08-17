def solution(distance, rocks, n):
    left, right = 0, distance
    rocks.sort()
    while left <= right:
        mid = (left + right) // 2
        current, remove = 0, 0
        min_dist = float('inf')
        for rock in rocks:
            dist = rock - current
            if dist < mid:
                remove += 1
            else:
                current = rock
                min_dist = min(min_dist, dist)
        if remove > n:
            right = mid - 1
        else:
            answer = min_dist
            left = mid + 1
    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))

# from itertools import combinations
# def solution(distance, rocks, n):
#     combination = combinations(rocks, len(rocks)-n)
#     big = []
#     for result in combination:
#         result = list(result)
#         result.insert(0, 0)
#         result.append(distance)
#         small = []
#         for i in range(len(result)-1):
#             small.append(abs(result[i+1]-result[i]))
#         big.append(min(small))
#     return max(big)
# print(solution(25, [2, 14, 11, 21, 17], 2))