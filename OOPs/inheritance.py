class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("General Animal Sound")
    
class Dog(Animal):#Dog inherits from Animal (Dog is a sublcass of Animal)
    def speak(self): # here we overide the speak method.
        print("Bark")
class Cat(Animal):
    def speak(self):
        print("Meow")
#create objects
my_dog= Dog("Rover")
my_cat=Cat("Fluffy")

#They both have a 'name' attritbutes (inherited from animal)
print(my_dog.name)
my_dog.speak()