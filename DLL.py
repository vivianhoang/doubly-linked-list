class Node(object):
    """Node Class."""
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None

class DLL(object):
    """Doubly Linked List Class."""
    def __init__(self):
        self.head = None
        self.tail = None

    # ASSUMING WE HAVE ALREADY CREATED A DLL LIST

    def len(self, node):
        """Checking the whole length of the DLL."""
        # to check the whole DLL, the "node" should be the list.head
        if not node:
            return 0
        else:
            return 1 + self.len(node.next)

    def add(self, position, name):
        """Adding a node."""
        if type(position) == int:
            if position < 0:
                print "Error. You are out of range."
            else if position > len(DLL.head):
                # creating the node here
                temp = Node(name)
                temp.previous = self.tail
                self.tail.next = temp
                self.tail = temp
                self.tail.next = None
                print "You have chosen a position that is out of range. Node was added to the end."
            else if position == 0:
                temp = Node(name)
                self.head.previous = temp.name
                temp.next = self.head
                self.head = temp
                self.head.previous = None
            else if position == len(DLL.head):
                temp = Node(name)
                temp.previous = self.tail
                self.tail.next = temp
                self.tail = temp
                self.tail.next = None
            else if 0 < position < len(DLL.head):
                count = 0
                temp = Node(name)
                current = self.head
                previous = None
                while count != position:
                    count += 1
                    previous = current
                    current = current.next
                previous.next = temp
                temp.previous = previous
                temp.next = current
                current.previous = temp
        if type(position) != int:
            print "Your position needs to be an integer."

    def remove(self, name):
        """Removing a node."""
        current = self.head
        previous = none

        while current is not None:
            if current == name:
                if previous is not None:
                    previous.next = current.next
                    current.next.previous = current.previous
                    break
                else:
                    self.head = current
                    self.head.previous = None
                    self.head.next = None

            previous = current
            current = current.next