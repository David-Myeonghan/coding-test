class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 항상 head 노드에서 어떻게 이동을 할지 생각.
#  -> current_node 이용
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


    def get_node(self, index):
        current_node = self.head
        current_index = 0

        while current_index != index:
            current_node = current_node.next
            current_index += 1

        return current_node


linked_list = LinkedList(5)
linked_list.append(12)
print(linked_list.get_node(1).data ) # -> 5를 들고 있는 노드를 반환해야 합니다!