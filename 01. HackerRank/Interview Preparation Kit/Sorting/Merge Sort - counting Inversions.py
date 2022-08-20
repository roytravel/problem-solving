"""
2
5
1 1 1 2 2
5
2 1 3 1 2
"""

def countInversions(arr, left, right):
    count = 0
    if right - left <= 1:
        return count

    mid = (right + left) // 2
    lcnt = countInversions(arr, left, mid)
    rcnt = countInversions(arr, mid, right)
    count += lcnt + rcnt

    merged = []
    i, j = left, mid
    while i < mid and j < right:
        if arr[i] > arr[j]:
            merged.append(arr[j])
            j += 1
            count += mid - i
        else:
            merged.append(arr[i])
            i += 1
    if i == mid:
        merged += arr[j:right]
    else:
        merged += arr[i:mid]

    arr[left:right] = merged
    return count


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = countInversions(arr, 0, n)
        print (result)