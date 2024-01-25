class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None


class Stack:

    def __init__(self):
        self.tail = None

    def push(self, data):
        node = Node(data)

        if self.tail is None:
            self.tail = node
        else:
            node.prev = self.tail
            self.tail = node

    def pop(self):
        node = None

        if self.tail is not None:
            node = self.tail
            self.tail = self.tail.prev

        return node