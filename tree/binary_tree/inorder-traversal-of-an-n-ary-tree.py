"""https://www.geeksforgeeks.org/inorder-traversal-of-an-n-ary-tree/"""


def inorder(self, node):
    if node == None:
        return
     
    # Total children count
    total = len(node.children)
         
    # All the children except the last
    for i in range(total-1):
        self.inorder(node.children[i])
         
    print(node.data)
         
    # Last child
    self.inorder(node.children[total-1])