class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, current, data):
        temp = current.prev
        next = Node(data, temp, current)
        current.prev = next
        temp.next = next 
        self.size += 1 

    def insert_back(self, current, data):
        temp = current.next
        next = Node(data, current, temp)
        temp.prev = next
        current.next = next
        self.size += 1

    def delete(self, current):
        front = current.prev
        back = current.next
        front.next = back
        front.prev = back
        self.size -= 1
        return current.data

    def search(self, target):
        current = self.head
        for i in range(self.size):
            if current.data == target:
                return i
            current = current.next
        return None

    def print_list(self):
        if self.is_empty():
            raise LookupError('There is no node in the linked list')
        else:
            current = self.head.next
            while current != self.tail:
                if current.next != self.tail:
                    print(current.data, '←→ ', end='')
                else:
                    print(current.data)
                current = current.next

D = DoublyLinkedList()
D.insert_back(D.head, 'apple') 
D.insert_front(D.tail, 'bear')
D.insert_front(D.tail, 'cat')
D.insert_back(D.head.next, 'dog')
D.print_list() # apple ←→ dog ←→ bear ←→ cat

print (D.search('cat'))

D.delete(D.tail.prev)
D.print_list() # apple ←→ dog ←→ bear

D.insert_front(D.tail.prev, 'fish') # apple ←→ dog ←→ bear ←→ fish ←→ cat
D.print_list()

D.delete(D.head.next) # dog ←→ bear ←→ fish ←→ cat
D.print_list()

D.delete(D.tail.prev) # dog ←→ bear ←→ fish
D.print_list()