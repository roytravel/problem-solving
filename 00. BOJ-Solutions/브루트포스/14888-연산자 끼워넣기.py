import sys
from itertools import permutations

def get_operations(in_operation: list) -> list:
    basic_operation = ['+', '-', '*', '/']
    operations : list = []
    for i in range(len(in_operation)): # [2, 1, 1, 1]
        for j in range(in_operation[i]):
            operations.append(basic_operation[i])
    
    return operations


def get_min_max_value(operations: list) -> None:
    global minimum, maximum
    for case in permutations(operations, N-1):
        total = numbers[0]
        for i in range(1, N):
            if case[i-1] == "+":
                total += numbers[i]
            
            elif case[i-1] == "-":
                total -= numbers[i]
                
            elif case[i-1] == "*":
                total *= numbers[i]
                
            elif case[i-1] == "/":
                total = int(total / numbers[i])
        
        if total > maximum:
            maximum = total
            
        if total < minimum:
            minimum = total


def dfs(depth, total, plus, minus, multiply, divide):
    if depth == N:
        global maximum, minimum
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    
    if plus:
        dfs(depth+1, total + numbers[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total - numbers[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total * numbers[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total / numbers[depth]), plus, minus, multiply, divide -1)
    
        
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    numbers = list(map(int, input().split()))
    in_operation = list(map(int, input().split()))
    maximum = -sys.maxsize
    minimum = sys.maxsize
    
    # Solution 1
    operations = get_operations(in_operation)
    get_min_max_value(operations)
    
    # Solution 2
    dfs(1, numbers[0], in_operation[0], in_operation[1], in_operation[2], in_operation[3])
    
    print (maximum)
    print (minimum)
