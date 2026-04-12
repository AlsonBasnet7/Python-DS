class Person:
    def __init__(self,name,age):
        self.name = name
        self._age= age

    @property # this makes "age" a property(the getter)

    def age(self):
        return self._age
    
    @age.setter # this defines the setter for the age property.
    def age(self,new_age):
        if new_age>=0 and new_age<=111:
            self._age = new_age
        else:
            print("Invalid age")


person = Person("Alson",22)
print(person.age)
