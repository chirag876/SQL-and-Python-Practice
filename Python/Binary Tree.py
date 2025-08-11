class Node:
    def __init__(self, data):
        self.data = data  # stores value
        self.left = None
        self.right = None


# Creating tree
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)
root.right.left = Node(70)


def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)  # Left subtree
        print(node.data, end=" ")  # root
        inorder_traversal(node.right)  # right subtree


print("Inorder Traversal")
inorder_traversal(root)
