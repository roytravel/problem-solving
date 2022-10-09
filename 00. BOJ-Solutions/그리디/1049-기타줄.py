import sys
input = sys.stdin.readline

N, M = map(int, input().split())
price = []
for _ in range(M):
    price.append(list(map(int, input().split())))
price.sort(key=lambda x:(x[0], x[1]))

six = sorted(price, key=lambda x:x[0])
one = sorted(price, key=lambda x:x[1])

package = six[0][0]
piece = one[0][1]

if package <= piece * 6: # 패키지로 사는 게 더 싸다면
    q, r = divmod (N, 6)
    answer = ((package * q) + (piece * r))
    if package < piece * r:
        answer = package * (q + 1)
else:
    answer = piece * N
print(answer)


# Wrong answer
# Q, R = divmod(N, 6)
# six = brand[0][0]
# total = 0
# if Q == 0:
#     brand.sort(key=lambda x:x[1])
#     one = brand[0][1]    
#     total = min(six, one * N)
# else:
#     packages = Q * six
#     brand.sort(key=lambda x:x[1])
#     one = brand[0][1]
#     pieces = R * one
#     total = packages + min (six, pieces)
# print (total)
###############################################
# if N <= 6:
#     six = brand[0][0]
#     brand.sort(key=lambda x:x[1])
#     one = brand[0][1] * N
#     print (min(six, one))
# else:
#     Q, R = divmod(N, 6)
#     total = 0
#     total += Q * brand[0][0]
#     six = brand[0][0]
#     brand.sort(key=lambda x:x[1])
#     temp1 = R * brand[0][1]
#     temp2 = min(six, temp1)
#     total += temp2
#     print (total)