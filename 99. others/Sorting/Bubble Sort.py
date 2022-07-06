class Sort:
    def __init__(self) -> None:
        pass

    def counting_sort(self, array : list) -> list:
        """ Best: O(n) Average: O(n+k) Worst: O(n+k) """
        count = [0] * (max(array) + 1)
        for num in array:
            count[num] += 1
        
        for i in range(1, len(count)):
            count[i] += count[i-1]
        
        result = [0] * len(array)
        for num in array:
            idx = count[num]
            result[idx - 1] = num
            count[num] = count[num] - 1

        return result

    def radix_sort(self, array : list) -> list:
        """ Best: O(n) Average: O(n) Worst: O(n)"""
        pass

    def shell_sort(self, array : list) -> list:
        """ Best: O(n) Average: O(n^1.3,1.5) Worst: O(n^2) | O(n) """
        pass

    def heap_sort(self, array : list) -> list:
        """ Best: O(nlogn) Average: O(nlogn) Worst: O(nlogn) | O(nlogn) """
        pass

    def merge_sort(self, array : list) -> list:
        """ Best: O(nlogn) Average: O(nlogn) Worst: O(nlogn) | O(nlogn) """
        pass

    def quick_sort(self, array : list) -> list:
        """ Best: O(nlogn) Average: O(nlogn) Worst: O(n^2) | O(nlogn) """
        pass

    def insert_sort(self, array : list) -> list:
        """ Best: O(n) Average: O(n^2) Worst: O(n^2) | O(n^2) """
        pass

    def bubble_sort(self, array : list) -> list:
        """ Best: O(n^2) Average: O(n^2) Worst: O(n^2) | O(n) """
        for i in range(len(array)):
            for j in range(len(array)-i-1):
                if array[j] > array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
        return array

    def selection_sort(self, array : list) -> list:
        """ Best: O(n^2) Average: O(n^2) Worst: O(n^2) | O(n^2) """
        pass


array = [1, 10, 5, 5, 2, 9, 8, 7, 6, 4, 0, 3, 2, 9]
sort = Sort()
#print (sort.bubble_sort(array))
print (sort.counting_sort(array))
