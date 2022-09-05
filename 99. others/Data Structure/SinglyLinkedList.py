class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, data): # O(1)
        if self.is_empty():
            self.head = Node(data, None)
        else:
            self.head = Node(data, self.head)
        self.size += 1

    def insert_back(self, data, current): # O(1)
        current.next = Node(data, current.next)
        self.size += 1
        
    def delete_front(self): # O(1)
        if self.is_empty():
            raise LookupError("There is no node in the linked list")
        self.head = self.head.next
        self.size -= 1

    def delete_back(self, current): # O(1)
        if self.is_empty():
            raise LookupError("There is no node in the linked list")
        temp = current.next
        current.next = temp.next
        self.size -= 1

    def traverse(self):
        array = []
        current = self.head
        while current:
            array.append(current.data)
            current = current.next
        return array

    def search(self, target):
        current = self.head
        for i in range(self.size):
            if current.data == target:
                return i
            current = current.next
        return None

    def print_list(self):
        current = self.head
        while current:
            if current.next != None:
                print (current.data, '→ ', end='')
            else:
                print (current.data)
            
            current = current.next

if __name__ == "__main__":
    S = SinglyLinkedList()

    # Insert
    S.insert_front('apple')
    S.insert_front('bear')
    S.insert_front('cat')
    S.insert_back('dog', S.head.next)
    S.insert_front('egg')
    S.insert_front('fish')

    # Search
    S.print_list() # fish → egg → cat → bear → dog → apple
    print(f"Index: {S.search('dog')}") # Index: 4
    
    # Delete
    S.delete_front() 
    S.print_list() # egg → cat → bear → dog → apple

    S.delete_back(S.head)
    S.print_list() # egg → bear → dog → apple

    # Traverse
    print (S.traverse()) # ['egg', 'bear', 'dog', 'apple']