A = int(input())
B = int(input())
C = int(input())
S = A + B + C
if A == 60 and B == 60 and C == 60:
    print ("Equilateral")
elif S == 180 and (A == B or B == C or A == C):
    print("Isosceles")
elif S == 180 and (A != B and B != C and A != C):
    print("Scalene")
elif S != 180:
    print ("Error")