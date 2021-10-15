class Node:
    
    def __init__(self, value, next, previous) -> None:
        self.value = value
        self.next = next
        self.previous = previous

class LinkedList:

    def __init__(self, tail=None) -> None:
        self.head = None
        self.tail = tail

    def add(self, element):
        if(self.tail == None):
            # If the list is empty, add this as the head of the list
            self.tail = element
            self.head = element
        else:
            self.tail.next = element
            element.previous = self.tail
            self.tail = element


    def get(self, index):
        elem = self.tail
        for i in range(index):
            elem = elem.previous

        return elem.value

    def pop(self):
        self.tail = self.tail.previous
        self.tail.next = None



l = LinkedList()
l.add(Node(10, None))
l.add(Node(25, None))
l.add(Node(26, None))
l.add(Node(15, None))
l.add(Node(19, None))


