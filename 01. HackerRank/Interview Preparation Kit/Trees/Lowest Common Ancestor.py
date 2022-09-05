class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break

                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def lca(root, v1, v2):
    value = sorted([v1, v2])
    v1, v2 = value[0], value[1]

    current = root
    while True:
        if current.info > v2:
            current = current.left
    
        elif current.info < v1:
            current = current.right

        elif v1 <= current.info <= v2:
            break

    return current


if __name__ == "__main__":
    tree = BinarySearchTree()
    t = int(input())

    array = list(map(int, input().split()))

    for i in range(t):
        tree.create(array[i])

    v = list(map(int, input().split()))

    answer = lca(tree.root, v[0], v[1])
    print (answer.info)
