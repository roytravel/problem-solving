# N을 0으로 만들면 이기는 게임! 3개나 1개를 가져갈 수 있음. 게임은 상근이 먼저시작
import sys
input = sys.stdin.readline

N = int(input())

if N % 2 == 1: 
    print ("SK")
else:
    print ("CY")

# winner = {1:"SK", 2:"CY", 3:"SK", 4:"CY", 5:"SK", 6:"CY"}
# turn = 1 # 홀수면 상근 짝수면 창영 승

# while True:
#     if N in winner_sk:
#         if turn % 2 == 1:
#             print(winner_sk[N])
#         else:
#             if winner_sk[N] == "SK":
#                 print ("CY")
#             else:
#                 print ("SK")
#     else:
#         if turn:
#             # 3개 가져갈 경우
#             if N - 3 == 0:
#                 print ("SK")
            
#             elif N - 1 ==0:
#                 print ("SK")
            
#             else:
#             # 1개 가져갈 경우 

#             turn = 0

#         else:

#             # 3개 가져갈 경우

#             # 1개 가져갈 경우 
            
#             turn = 1