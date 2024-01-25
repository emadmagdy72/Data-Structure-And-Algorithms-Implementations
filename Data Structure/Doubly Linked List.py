class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        node = Node(data)

        # if linked list is empty
        if self.head is None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def insert(self, loc, data):
        node = Node(data)

        # if linkedlist is empty
        if self.head is None:
            self.head = node
            self.tail = node

        else:
            if loc == 0:
                node.next = self.head
                self.head.prev = node
                self.head = node
            else:
                curr = self.head
                count = 0
                while count < loc - 1 and curr is not None:
                    curr = curr.next
                    count += 1

                # if loc in the last node
                if curr == self.tail or curr is None:
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
                else:
                    node.next = curr.next
                    node.prev = curr
                    curr.next.prev = node
                    curr.next = node

    def search(self, data):
        curr = None

        if self.head is not None:
            curr = self.head
            while curr is not None and curr.data != data:
                curr = curr.next

        return curr

    def delete(self, loc):

        flag = 0

        if self.head is not None:

            if loc == 0:
                # if one node in linked list
                if self.head == self.tail:
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
                flag = 1
            else:
                count = 0
                curr = self.head

                while count < loc and curr is not None:
                    count += 1
                    curr = curr.next

                # if node out of range
                if curr is not None:
                    # curr in the last node
                    if curr == self.tail:
                        self.tail = self.tail.prev
                        self.tail.next = None
                    else:
                        curr.prev.next = curr.next
                        curr.next.prev = curr.prev
                    flag = 1

        return flag

    def length(self):
        count = 0
        if self.head is not None:
            curr = self.head
            while curr is not None:
                curr = curr.next
                count += 1
        return count

    def reverse(self):
        curr = self.head
        prev = None

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    def displayNodes(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next



