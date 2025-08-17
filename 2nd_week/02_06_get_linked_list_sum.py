class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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

    def add_node(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        prev_node = self.get_node(index - 1)
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

# 생각:
# 링크드 리스트의 모든 노드를 한번씩 방문해서 각 노드의 value를 문자열로 저장
## 링크드 리스트의 총 노드 갯수 구하기
# for-loop => value 저장

# 실제 해답:
# 순회는 맞았으나, for-loop이라는 리스트를 위한 고정관념에 갖힘.
# 문자열로 저장이 아니라, * 10 + current_node.data

def linked_list_sum(linked_list):
    sum = 0
    current_node = linked_list.head

    while current_node is not None:
        if sum != 0:
            sum = sum * 10 + current_node.data
        else:
            sum = current_node.data
        current_node = current_node.next

    return sum


# 두 개 링크드 리스트 합
def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = linked_list_sum(linked_list_1)

    sum_2 = 0
    current_node_2 = linked_list_2.head

    while current_node_2 is not None:
        if sum_2 != 0:
            sum_2 = sum_2 * 10 + current_node_2.data
        else:
            sum_2 = current_node_2.data
        current_node_2 = current_node_2.next

    return sum_1 + sum_2



linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))