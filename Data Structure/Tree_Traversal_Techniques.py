class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class TreeTraversal:

    def InOrder(self, root):
        if root:
            self.InOrder(root.left)
            print(root.val)
            self.InOrder(root.right)

    def PreOrder(self, root):
        if root:
            print(root.val)
            self.PreOrder(root.left)
            self.PreOrder(root.right)

    def PostOrder(self, root):
        if root:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print(root.val)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

traversal = TreeTraversal()
print('*'*10 + 'InOrder' + '*'*10)
traversal.InOrder(root)
print('*'*10 + 'PreOrder' + '*'*10)
traversal.PreOrder(root)
print('*'*10 + 'PostOrder' + '*'*10)
traversal.PostOrder(root)

