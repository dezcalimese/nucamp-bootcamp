class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        # Adding a node to an empty list
        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return

        # Adding a node to a list that isn't empty
        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Appended new Node with value:", node.next.value)

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
        elif self.head is not None:
            new_node = Node(value)
            node = self.head
            new_node.next = node
            print("Prepended new Head Node with value:", new_node.value)
            print("Node following Head is:", new_node.next.value)


llist = LinkedList()
llist.prepend("First Node")
llist.prepend("Inserted New First Node")
