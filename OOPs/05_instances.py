class Employee:
    company="Telsa" #This is the class attributes.
    def __init__(self,name,caste, company):
        self.name=name
        self.caset=caste
        self.company=company
    def get_name(self):
        return self.get_name
    def get_caste(self):
        print(f"{self.name} is the first name of the Employee.And {self.caste} is the second name of the employee")
    
e1=Employee("Alson","Basnet","yeti airlines")
print(e1.company)#will always print the instance variable whenever present.
# object introspection
print(dir(e1))#this converts the value in the dictonary