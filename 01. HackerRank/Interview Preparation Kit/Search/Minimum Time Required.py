# Solution
import math
def minTime(machines, goal):
    minday = math.ceil(goal / (len(machines) / min(machines)))
    maxday = math.ceil(goal / (len(machines) / max(machines)))
    
    while minday < maxday:
        day = (minday + maxday) // 2        
        prod = sum([day//i for i in machines])
        if prod >= goal:
            maxday = day
        else:
            minday = day + 1
    return maxday

# # Time over 5/14, Success 9/14
# def minTime(machines, goal):
#     day = 0
#     machines.sort()
#     while True:
#         day += 1
#         prod = 0
#         for i in range(len(machines)):
#             q, _ = divmod(day, machines[i])
#             prod += q
#             if prod >= goal:
#                 return day

# # Wrong answer
# def minTime(machines, goal):
#     day = max(machines)-1
#     while True:
#         day += 1
#         prod = 0
#         for i in range(len(machines)):
#             q, _ = divmod(day, machines[i])
#             prod += q
#             if prod >= goal:
#                 return day

# # Time over 6/14, Success 8/14
# def minTime(machines, goal):
#     day = 0
#     while True:
#         day += 1
#         production = 0
#         for i in range(len(machines)):
#             q, r = divmod(day, machines[i])
#             production += q
#             if production >= goal:
#                 return day
    
if __name__ == '__main__':
    nGoal = input().split()
    n = int(nGoal[0])
    goal = int(nGoal[1])
    machines = list(map(int, input().rstrip().split()))
    ans = minTime(machines, goal)
    print (ans)
