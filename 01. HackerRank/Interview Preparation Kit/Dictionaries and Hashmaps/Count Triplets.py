from collections import defaultdict

def countTriplets(arr, r):
    total = 0
    single, double = defaultdict(int), defaultdict(int)
    for n in arr:
        if n % r == 0:
            total += double[n//r]
            double[n] += single[n//r]
        single[n] += 1
    print (single, double)
    return total


n, r = 6, 3
arr = [1, 3, 9, 9, 27, 81]
print(countTriplets(arr, r))