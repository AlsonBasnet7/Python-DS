#claass is basically a blue or template.
#object is bascially a instance created from the template(class)
class Employee:
    brand ="Honda"
    def get_salary(self):#self is important here because self is the way to reference the object of the class which is being created.
        print(self)
        return 200
e= Employee()# An object of the class employee is created here.
print(e.get_salary())
