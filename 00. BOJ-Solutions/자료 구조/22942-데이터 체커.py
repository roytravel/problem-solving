import sys
input = sys.stdin.readline

N = int(input())
circles = []
for i in range(N):
    x, r = map(int, input().split())
    circles.append([x-r, i, 0]) # start
    circles.append([x+r, i, 1]) # end

circles.sort() # This is key point: It represents the dot as a vertical coordinate system.
stack = []

for i in range(N):
    way = circles[i][2]
    if way == 0: # the case when it's start
        stack.append(circles[i])
    else: # the case when it's end
        if stack[-1][2] == 0:
            if stack[-1][1] == circles[i][1]: # the case when index is same.
                stack.pop()
            else:
                print ("NO")
                exit()
print ("YES")





# Time over
# import sys
# input = sys.stdin.readline

# N  = int(input())
# circles = []
# for _ in range(N):
#     a, b = map(int, input().split())
#     circles.append([a, b])

# circles.sort(key=lambda x:x[0])
# region = []

# for x, r in circles:
#     start = x - r
#     end = x + r

#     if start in region or end in region:
#         print("NO")
#         exit()
#     else:
#         region.append(start)
#         region.append(end)

# print ("YES")