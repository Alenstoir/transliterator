class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return self.data


class Dll:
    def __init__(self):
        self.head = Node(None)

    def __iter__(self):
        while self.head.prev is not None:
            self.head = self.head.prev
        return self

    def __next__(self):
        if self.head.next is not None:
            self.head = self.head.next
        else:
            raise StopIteration
        return self.head

    def add(self, data):
        new_node = Node(data)
        new_node.prev = self.head
        if self.head is not None:
            while self.head.next is not None:
                self.head = self.head.next
            self.head.next = new_node
        self.head = new_node
