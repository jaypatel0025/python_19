class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def describe(self):
        return f"{self.name} is {self.age} years old"

student1=Student("jay",21)
print(student1.describe())

student2=Student("mohit",24)
print(student2.describe())
