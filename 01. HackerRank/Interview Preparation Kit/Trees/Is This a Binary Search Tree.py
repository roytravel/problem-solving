def checkBST(root):
    return check(root, -1, 100000)
    
def check(root, min, max):
    if root == None:
        return True
    
    if root.data <= min or root.data >= max:
        return False    
    
    return check(root.left, min, root.data) and check(root.right, root.data, max)