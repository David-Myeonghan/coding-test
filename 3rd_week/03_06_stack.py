class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 1. 한 곳에서만 자료를 넣고 뺄 수 있다.
# 2. LIFO -> Last In First Out --> 가장 마지막에 넣은게 제일 빨리 나온다.
# 맨 위에 있는 값만 알면 된다.
# push: 맨 위에 값 넣기
# pop: 맨 위에 값 빼기
# peek: 맨 위의 값 보기

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            print('Stack is empty')
        deleted_head = self.head
        self.head = self.head.next
        return deleted_head

    def peek(self):
        if self.is_empty():
            print('Stack is empty')
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None

# stack = Stack()
# stack.push(1)
# print(stack.peek())
# stack.push(2)
# print(stack.peek())
# stack.push(3)
# print(stack.peek())
# stack.pop()
# print(stack.peek())
# stack.pop()
# stack.pop()
# print(stack.peek())
#
