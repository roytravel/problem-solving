# import sys
# input = sys.stdin.readline

# A, B = list(map(int, input().split()))

# count = 1
# while True:
#     if str(B)[-1] == '1':
#         B = int(str(B)[:-1])
#         count +=1
        
#     elif B / 2 >= A:
#         B = B // 2
#         count +=1

#     if B == A:
#         print (count)
#         break

#     elif B < A:
#         print (-1)
#         break

# import sys
# input = sys.stdin.readline

# A, B = list(map(int, input().split()))

# count = 1
# while True:    
#     if B % 10 == 1:
#         B = B // 10
#         count +=1
    
#     elif B % 2 == 0:
#         B = B // 2 
#         count +=1

#     if B == A:
#         print (count)
#         break

#     elif B < A:
#         print (-1)
#         break

# 아래가 답인데 솔직히 이해안감 왜 temp = B ...?
import sys
input = sys.stdin.readline

A, B = list(map(int, input().split()))
count = 1
while B != A:
    temp = B
    if B % 10 == 1:
        B = B // 10
        count +=1
    
    elif B % 2 == 0:
        B = B // 2 
        count +=1

    if temp == B:
        print (-1)
        break
else:
    print (count)