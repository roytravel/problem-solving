A = int(input())
B = int(input())
C = int(input())
D = int(input())
science = [A, B, C, D]
science.sort(reverse=True)
E = int(input())
F = int(input())
print (sum(science[:3])+max(E, F))