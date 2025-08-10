class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)
print(node.data, node.next)

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # Add a new node to the last node
    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.next = Node(value)

    # Print all element from the head
    def print_all(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next


linked_list = LinkedList(5)
# print(linked_list.head.data)

linked_list.append(12)
linked_list.append(8)
linked_list.print_all()