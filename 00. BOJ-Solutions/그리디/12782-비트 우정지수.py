import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(str, input().split())
    count0, count1 = 0, 0
    
    for i in range(len(a)):
        if a[i] != b[i]:
            if a[i] == "1":
                count1 += 1
            elif a[i] == "0":
                count0 += 1
    print (max(count1, count0))
    
# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     a, b = map(str, input().split())
#     count = 0
#     for i in range(len(a)-1):
#         if a[i] != b[i] and a[i+1] != b[i+1]:
#             count += 1
#         elif a[i] != b[i] and a[i+1] == b[i+1]:
#             count += 1
        
#     print (count)