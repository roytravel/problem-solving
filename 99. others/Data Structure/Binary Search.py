def binary_search(array, target):
    start, end = 0, len(array)-1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] < target:
            start = mid + 1
        
        elif array[mid] > target:
            end = mid - 1 
              

def binary_search_recursion(array, start, end, target):
    if start > end:
        return 

    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    elif array[mid] < target:
        start = mid + 1
    
    elif array[mid] > target:
        end = mid - 1

    return binary_search_recursion(array, start, end, target)


if __name__ == "__main__":
    target = 5
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # recursive binary search
    start, end = 0, len(array)-1
    index = binary_search_recursion(array, start, end, target)
    print (index)

    # binary search
    index = binary_search(array, target)
    print (index)