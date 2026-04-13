class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):  # Getter
        return self._name

    @name.setter
    def name(self, new_name):  # Setter
        self._name = new_name 

    @name.deleter
    def name(self):
        del self._name

p = Person("Alice")
print(p.name)  # Alice
del p.name
print(p.name)  # AttributeError: 'Person' object has no attribute '_name'