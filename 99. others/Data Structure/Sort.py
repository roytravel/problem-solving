class Sort:
    def __init__(self) -> None:
        pass

    def counting_sort(self, array : list) -> list:
        """ Best: O(n) Average: O(n+k) Worst: O(n+k) """
        count = [0] * (max(array) + 1) # 1. create a count array to check how many numbers each have.
        
        for num in array: # 2. check how many numbers each have.
            count[num] += 1

        for i in range(1, len(count)): # 3. do cumulative sum
            count[i] += count[i-1]

        arr = [0] * len(array) # 4. create a new array to contain the numbers to be sorted.

        for num in array: # 5. sort.
            idx = count[num]
            arr[idx-1] = num
            count[num] -= 1
        
        return arr

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
        """ Best: O(nlogn) Average: O(nlogn) Worst: O(nlogn) | O(n) """
        if len(array) < 2:
            return array

        mid = len(array) // 2
        low = self.merge_sort(array[:mid])
        high = self.merge_sort(array[mid:])

        merged_array = []
        l, h = 0, 0
        while l < len(low) and h < len(high):
            if low[l] < high[h]:
                merged_array.append(low[l])
                l += 1
            else:
                merged_array.append(high[h])
                h += 1
        
        merged_array += low[l:]
        merged_array += high[h:]

        return merged_array

    def quick_sort(self, array : list) -> list:
        """ Best: O(nlogn) Average: O(nlogn) Worst: O(n^2) | O(nlogn) """
        if len(array) <= 1:
            return array

        pivot = array[len(array) // 2]
        small, big, equal = [], [], []

        for n in array:
            if n < pivot:
                small.append(n)
            elif n > pivot:
                big.append(n)
            else:
                equal.append(n)
        
        return self.quick_sort(small) + equal + self.quick_sort(big)

    def _quick_sort(self, array : list) -> list:
        """ Pythonic version of quick sort """
        if len(array) <= 1:
            return array

        pivot, arr = array[0], array[1:]
        small = [n for n in arr if n < pivot]
        big = [n for n in arr if n > pivot]

        return self._quick_sort(small) + [pivot] + self._quick_sort(big)


    def insert_sort(self, array : list) -> list:
        """ Best: O(n) Average: O(n^2) Worst: O(n^2) | O(n^2) """
        # 1. Optimization code
        for i in range(1, len(array)):
            j = i
            while j > 0 and array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                j -= 1
        return array

         # 2. General code
        for i in range(1, len(array)):
            for j in range(i, 0, -1):
                if array[j-1] > array[j]:
                    array[j-1], array[j] = array[j], array[j-1]
        return array

    def bubble_sort(self, array : list) -> list:
        """ Best: O(n^2) Average: O(n^2) Worst: O(n^2) | O(n) """
        for i in range(len(array)):
            for j in range(len(array)-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array

    def selection_sort(self, array : list) -> list:
        """ Best: O(n^2) Average: O(n^2) Worst: O(n^2) | O(n^2) """
        pass


array = [1, 10, 5, 5, 2, 9, 8, 7, 6, 4, 0, 3, 2, 9]
sort = Sort()
#print (sort.bubble_sort(array))
#print (sort.insert_sort(array))
#print (sort.merge_sort(array))
#print (sort.quick_sort(array))
#print (sort._quick_sort(array))
print (sort.counting_sort(array))