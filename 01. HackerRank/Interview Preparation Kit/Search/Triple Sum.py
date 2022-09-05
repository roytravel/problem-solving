# Success
def triplets(a, b, c):
    a = list(set(sorted(a)))
    b = list(set(sorted(b)))
    c = list(set(sorted(c)))
    count = 0
    for i in range(len(b)):
        starta, enda = 0, len(a)-1
        while starta <= enda:
            mida = (starta+enda) // 2
            if b[i] >= a[mida]:
                starta = mida + 1
            else:
                enda = mida - 1
        
        startc, endc = 0, len(c)-1
        while startc <= endc:
            midc = (startc+endc) // 2
            if b[i] >= c[midc]:
                startc = midc + 1
            else:
                endc = midc - 1
        
        count += starta * startc
    return count


# # Runtime error 5/10
# def triplets(a, b, c):
#     a = list(set(sorted(a)))
#     b = list(set(sorted(b)))
#     c = list(set(sorted(c)))
#     count = 0
#     for i in range(len(b)):
#         starta, enda = 0, lena-1
#         while starta <= enda:
#             mida = (starta+enda) // 2
#             if b[i] >= a[mida]:
#                 starta = mida + 1
#             else:
#                 enda = mida - 1
        
#         startc, endc = 0, lenc-1
#         while startc <= endc:
#             midc = (startc+endc) // 2
#             if b[i] >= c[midc]:
#                 startc = midc + 1
#             else:
#                 endc = midc - 1
        
#         count += starta * startc
    
#     return count

# # Wrong 5/10
# def triplets(a, b, c):
#     a = list(set(sorted(a)))
#     b = list(set(sorted(b)))
#     c = list(set(sorted(c)))
#     count = 0
#     for i in range(lenb):
#         starta, enda = 0, lena-1
#         while starta <= enda:
#             mida = (starta+enda) // 2
#             if b[i] >= a[mida]:
#                 starta = mida + 1
#             else:
#                 enda = mida - 1
        
#         startc, endc = 0, lenc-1
#         while startc <= endc:
#             midc = (startc+endc) // 2
#             if b[i] >= c[midc]:
#                 startc = midc + 1
#             else:
#                 endc = midc - 1
        
#         count += starta * startc
    
#     return count


# # Time over 5/10
# def triplets(a, b, c):
#     a.sort()
#     b = list(set(sorted(b)))
#     c.sort()
#     count = 0
#     for i in range(len(b)):
#         a_arr, b_arr, c_arr = [], [], []
#         for j in range(len(a)):
#             if b[i] >= a[j]:
#                 a_arr.append(a[j])
#             else:
#                 break
#         for j in range(len(c)):
#             if b[i] >= c[j]:
#                 c_arr.append(c[j])
#             else:
#                 break
        
#         count += len(set(a_arr)) * len(set(c_arr))
    
#     return count
        
if __name__ == '__main__':
    lenaLenbLenc = input().split()
    lena = int(lenaLenbLenc[0])
    lenb = int(lenaLenbLenc[1])
    lenc = int(lenaLenbLenc[2])
    arra = list(map(int, input().rstrip().split()))
    arrb = list(map(int, input().rstrip().split()))
    arrc = list(map(int, input().rstrip().split()))
    ans = triplets(arra, arrb, arrc)
    print (ans)