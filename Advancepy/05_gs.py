class Person:
    def __init__(self,name):
        self._name=name
    @property
    def name(self): #getter
        return self._name
    @name.setter
    def name(self,new_name): #setter
        self._name=new_name
p =Person("Alice")
print(p.name)
p.name="bob"
print(p.name)

