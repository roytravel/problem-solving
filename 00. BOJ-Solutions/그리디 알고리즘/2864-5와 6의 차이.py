A, B = map(str, input().split())
if "6" in A or "6" in B:
    A = A.replace("6","5")
    B = B.replace("6","5")
_min = sum(map(int, [A, B]))

if "5" in A or "5" in B:
    A = A.replace("5","6")
    B = B.replace("5","6")
_max = sum(map(int, [A, B]))
print (_min, _max)