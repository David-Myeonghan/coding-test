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

    # Add a node at the indexed position
    # 인덱스 위치에 value를 가진 Node 추가
    def add_node(self, index, value):
        new_node = Node(value)

        # index 가 0이라면,
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return


        #  index - 1 번째의 노드가 필요.
        prev_node = self.get_node(index - 1)

        # 연결이 끊어지지 않도록 prev_node의 다음 노드를 기억할 필요
        next_node = prev_node.next

        prev_node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return

        prev_node = self.get_node(index - 1)
        index_node = self.get_node(index)
        prev_node.next = index_node.next

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
# linked_list.print_all()
# linked_list.add_node(1, 6)
# linked_list.print_all()
linked_list.delete_node(1)
linked_list.print_all()
