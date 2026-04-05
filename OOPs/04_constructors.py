#we use constructor to initilize the object.
# init plays the important role here.
# the init is special method.
class Info:
    def __init__(self,name,caste):# the constructor
        self.name = name #setting the name attributes
        self.caste = caste #setting the caste attributes
    # when we do this:
    # the init method is automatically called
my_name= Info("Alson","Basnet")
print(my_name.name)

# print(my_name)
# class Dog:
#     def __init__(self, name, breed):  # The constructor
#         self.name = name      # Setting the name attribute
#         self.breed = breed    # Setting the breed attribute

# # When we do this:
# my_dog = Dog("Fido", "Poodle")  # The __init__ method is automatically called

# # It's like we're saying:
# # 1. Create a new Dog object.
# # 2. Run the __init__ method on this new object:
# #    - Set my_dog.name to "Fido"
# #    - Set my_dog.breed to "Poodle"
# class Dog:
#     def __init__(self, name="Unknown", breed="Mixed"):
#         self.name = name
#         self.breed = breed

# dog1 = Dog()          # name will be "Unknown", breed will be "Mixed"
# dog2 = Dog("Rex")     # name will be "Rex", breed will be "Mixed"
# dog3 = Dog("Bella", "Labrador") # name will be "Bella", breed will be "Labrador"