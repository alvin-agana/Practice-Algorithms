"""
Implementation of a binary search tree.
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = root
        print("Initializing tree with root of {a}".format(a=root.value))

    def preOrderTraversal(self, node):
        if node:
            print(node.value)
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)
            
    def inOrderTraversal(self, node):
        if node:
            self.inOrderTraversal(node.left)
            print(node.value)
            self.inOrderTraversal(node.right)

    def postOrderTraversal(self, node):
        if node:
            self.postOrderTraversal(node.left)
            self.postOrderTraversal(node.right)
            print(node.value)

tree = BinaryTree(Node(1))
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.left.left.left = Node(8)
tree.root.left.left.right = Node(9)
tree.root.left.right.left = Node(10)
tree.root.left.right.right = Node(11)
tree.root.right.left.left= Node(12)
tree.root.right.left.right = Node(13)
tree.postOrderTraversal(tree.root)

