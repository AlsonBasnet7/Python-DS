class iic:
    
    def __init__(self,name,faculty):
        self.name=name
        self.faculty=faculty

    def isStudnet(self):
        print(f"{self.name} Welcomes, you in IIC")
student1=iic("Alson","BIT")
print(student1.name)

