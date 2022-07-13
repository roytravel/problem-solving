# # A = 낮에 올라갈 수 있는 미터
# # B = 밤에 잠자는 동안 내려가는 미터 
# # V = 목표 높이

# A, B, V = list(map(int, input().split()))
# got_dist = 0
# day = 1

# for i in range(1, 1000000000000):
#     # 낮
#     got_dist += A

#     # 낮에 올라간 것이 목표치에 도달했다면 출력
#     if got_dist >= V:
#         print (day)
#         break

#     else:
#         got_dist -= B
#         day += 1


A, B, V = list(map(int, input().split()))
height = 0
day = 0

while True:
    day += 1
    if height >= V:
        print (day)
        break
    else:
        height -= B