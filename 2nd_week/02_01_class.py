class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is %d years old' % (self.name, self.age))

person1 = Person('John', 20)
# print(person1)
person1.talk()
