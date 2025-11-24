# 충돌시,
# 1. Chaining 기법: 충돌이 발생했을 때, 그 값들을 링크드 리스트로 관리한다.

class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

# linked_tuple = LinkedTuple()
#
# linked_tuple.add('a', 1)
# linked_tuple.add('b', 2)
#
# print(linked_tuple.items)
# print(linked_tuple.get('b'))

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)

my_dict = LinkedDict()

my_dict.put('test', 3)
print(my_dict.get('test'))


