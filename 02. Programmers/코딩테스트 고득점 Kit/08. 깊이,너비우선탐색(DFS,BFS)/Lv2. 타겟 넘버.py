def solution(numbers, target): # DFS
    answer = 0
    SUM = 0
    n = len(numbers)
    def dfs(depth, SUM):
        if depth == n:
            if SUM == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(depth+1, SUM+numbers[depth])
            dfs(depth+1, SUM-numbers[depth])
    dfs(0, 0)
    return answer

def solution(numbers, target): #BFS
    answer = 0
    leaves = [0]
    for num in numbers:
        temp = []
        for leaf in leaves:
            temp.append(leaf + num)
            temp.append(leaf - num)
        leaves = temp
    
    for leaf in leaves:
        if leaf == target:
            answer += 1
    
    return answer

#print (solution([1, 1, 1, 1, 1], 3))
# print (solution([4, 1, 2, 1], 4))


# Time Over
# from itertools import combinations
# def solution(numbers, target): # Brute force
#     answer = 0
#     sign = ["+", "-"] * len(numbers)
#     permutation = combinations(sign, len(numbers))
#     temp = []
#     for result in list(permutation):
#         if result in temp:
#             continue
#         else:
#             temp.append(result)
#         equation = ""
#         for i in range(len(result)):
#             equation += result[i]
#             equation += str(numbers[i])
#         if eval(equation) == target:
#             answer +=1
#     return answer

# print (solution([1, 1, 1, 1, 1], 3))
# print (solution([4, 1, 2, 1], 4))