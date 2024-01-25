class Node:
    def __init__(self, data):
        self.data = data
        self.next = None




class Queue:
    def __init__(self):
        self.tail = None
        self.head = None

    def enqueue(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        node = None

        if self.head is not None:
            node = self.head
            self.head = node.next
            if self.head is None:
                self.tail = None

        return node

