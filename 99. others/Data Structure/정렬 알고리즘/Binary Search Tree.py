class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.value)


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(value)
                        break
                elif value > current.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(value)
                        break
                else:
                    break
    

    def search(self, value):
        current = self.root
        while current:
            if current.value == value:
                return True
            elif current.value > value:
                current = current.left
            else:
                current = current.right
        return False


    def delete(self, value):
        """ Check if there is node that has to delete else return False 
        after checking, node that will be deleted is 'current', 
        parent node of node that will be deleted become 'parent' """
        is_search = False
        current = self.root
        parent = self.root
        while current:
            if current.value == value:
                is_search = True
                break
            elif value < current.value:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right

        if is_search == False:
            return False
		
        # The case when node that will be deleted has no child
        if current.left == None and current.right == None: 
            if value < parent.value:
                parent.left = None
            else:
                parent.right = None
        
        # The case when node that will be deleted only has left child. 
        if current.left != None and current.right == None: # The case 
            if value < parent.value:
                parent.left = current.left
            else:
                parent.right = current.left
        
        # The case when node that will be deleted only has right child.
        if current.left == None and current.right != None:
            if value < parent.value:
                parent.left = current.right
            else:
                parent.right = current.right                

        # The case when node that will be deleted has two child: left, right
        if current.left != None and current.right != None:
            change = current.right
            change_parent = current.right
            while change.left != None:
                change_parent = change
                change = change.left

            if change.right != None:
                change_parent.left = change.right
            else:
                change_parent.left = None
                
            if value < parent.value:
                parent.left = change
                change.right = current.right
                change.left = current.left
            else:
                parent.right = change
                change.left = current.left
                change.right = current.right

        return True

if __name__ == "__main__":
    array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

    BST = BinarySearchTree()
    for x in array:
        BST.insert(x)

    print(BST.search(55))
    print(BST.search(14))
    print(BST.search(48))

    print(BST.delete(55))
    print(BST.delete(14))
    print(BST.delete(11))