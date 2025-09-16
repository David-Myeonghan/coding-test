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

    def get_kth_node_from_last(self, k):
        # 1. 링크드 리스트의 끝을 모르기 때문에, 끝을 먼저 알아내자. (길이를 구한다.)
        # 2. 리스트의 길이에서 k 만큼 빼고, 그만큼 이동시킨다.
        # -> 한바퀴 돌아서 링크드 리스트의 길이를 알아낸 다음, 그 길이에서 k만큼을 뺀 순서의 노드를 반환.
        length = 1
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            length += 1
        print('length: ',length)
        end_length = length - k # 끝(length)에서 k번째 --> length - k
        cur = self.head

        for i in range(end_length):
            cur = cur.next

        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!