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
        from collections import deque
        buckets = [deque() for _ in range(10)]
        MAX = max(array)
        queue = deque(array)
        radix = 1

        while MAX >= radix:
            while queue:
                num = queue.popleft()
                buckets[(num // radix) % 10].append(num)

            for bucket in buckets:
                while bucket:
                    queue.append(bucket.popleft())

            radix *= 10

        return list(queue)


    def shell_sort(self, array : list) -> list:
        """ Best: O(n) Average: O(n^1.3,1.5) Worst: O(n^2) | O(n) """
        n = len(array)
        h = n // 2 # h = interval
        while h > 0:
            for i in range(h, n):
                j = i - h
                temp = array[i]
                while j >= 0 and array[j] > temp:
                    array[j+h] = array[j]
                    j -= h
                array[j+h] = temp
            h //= 2

        return array


    def heap_sort(self, array : list) -> list:
        """ Best: O(nlogn) Average: O(nlogn) Worst: O(nlogn) | O(nlogn) """
        n = len(array)

        for i in range(n//2-1, -1, -1):
            self._heapify(array, i, n)
        
        for i in range(n-1, 0, -1):
            array[0], array[i] = array[i], array[0]
            self._heapify(array, 0, i)

        return array


    def _heapify(self, array : list, index : int, heap_size : int) -> None:
        biggest = index
        left = (2 * index) + 1
        right = (2 * index) + 2

        if left < heap_size and array[left] > array[biggest]:
            biggest = left
        
        if right < heap_size and array[right] > array[biggest]:
            biggest = right
        
        if biggest != index:
            array[biggest], array[index] = array[index], array[biggest]
            self._heapify(array, biggest, heap_size)


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
        mid = [n for n in arr if n == pivot]
        big = [n for n in arr if n > pivot]

        return self._quick_sort(small) + [pivot] + mid + self._quick_sort(big)


    def insert_sort(self, array : list) -> list:
        """ Best: O(n) Average: O(n^2) Worst: O(n^2) | O(n^2) """ # 1. Optimization code
        for i in range(1, len(array)):
            j = i
            while j > 0 and array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                j -= 1
        return array


    def _insert_code(self, array : list) -> list:
        """ Best: O(n) Average: O(n^2) Worst: O(n^2) | O(n^2) """ # 2. General code
        for i in range(1, len(array)):
            for j in range(i, 0, -1):
                if array[j-1] > array[j]:
                    array[j-1], array[j] = array[j], array[j-1]
        return array


    def bubble_sort(self, array : list) -> list:
        """ Best: O(n^2) Average: O(n^2) Worst: O(n^2) | O(n) """
        n = len(array)
        for i in range(n):
            for j in range(n-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array


    def selection_sort(self, array : list) -> list:
        """ Best: O(n^2) Average: O(n^2) Worst: O(n^2) | O(n^2) """
        n = len(array)
        for i in range(n):
            idx = i
            for j in range(i+1, n):
                if array[idx] > array[j]:
                    idx = j
            array[idx], array[i] = array[i], array[idx]
        return array


if __name__ == "__main__":
    array = [1, 10, 5, 5, 2, 9, 8, 7, 6, 4, 0, 3, 2, 9]
    sort = Sort()
    print (sort.selection_sort(array))
    print (sort.bubble_sort(array))
    print (sort.insert_sort(array))
    print (sort.merge_sort(array))
    print (sort.quick_sort(array))
    print (sort._quick_sort(array))
    print (sort.counting_sort(array))
    print (sort.heap_sort(array))
    print (sort.shell_sort(array))
    print (sort.radix_sort(array))