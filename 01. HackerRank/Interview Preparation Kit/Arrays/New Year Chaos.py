def minimumBribes(n, q):
    for i, j in enumerate(q, start=1):
        if j - i > 2:
            print ("Too chaotic")
            return
    count = 0
    for i in range(1, n):
        j = i
        while j > 0 and q[j-1] > q[j]: # Optimized insert sort.
            q[j-1], q[j] = q[j], q[j-1]
            j -= 1
            count += 1
    print (count)


t = int(input().strip())
for t_itr in range(t):
    n = int(input().strip())
    q = list(map(int, input().rstrip().split()))

    minimumBribes(n, q)


# import sys
# def minimumBribes(q):
#     bribe = 0
#     MINS = [sys.maxsize, sys.maxsize]
#     for i, p in reversed(list(enumerate(q, start=1))):
#         if p - i > 2:
#             print("Too chaotic")
#             return
        
#         elif p > MINS[1]:
#             bribe += 2
#         elif p > MINS[0]:
#             bribe += 1
        
#         if p < MINS[0]:
#             MINS = (p, MINS[0])
#         elif p < MINS[1]:
#             MINS = (MINS[0], p)
#     print (bribe)


# def minimumBribes(q):
#     bribe = 0
#     for i, p in enumerate(q, start=1):
#         if p - i > 2:
#             print("Too chaotic")
#             return

#         for j in range(i, len(q)):
#             if p > q[j]:
#                 bribe += 1
#     print (bribe)


# def minimumBribes(q):
#     # Write your code here
#     bribe = 0
#     q.insert(0, 0)
#     count = [0] * (len(q)+1)
#     end = False
#     for i in range(1, len(q)+1):
#         value = q[i] - i
#         if value >= 3:
#             print ("Too chaotic")
#             end = True
#             break
#         else:
#             if value >= 0:
#                 bribe += q[i] - i
#             else:
#                 if i != len(q):
#                     if q[i] > q[i+1]:
#                         bribe += 1
#     if not end:
#         print (bribe)