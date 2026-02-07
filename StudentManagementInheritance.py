class Person:
    def getDataGeneral(self,name,age,gender,idnumber):
        self.name=name
        self.age=age
        self.gender=gender
        self.idnumber=idnumber
    def putDataGeneral(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("ID Number:",self.idnumber)

class Student(Person):
    def getDataStudent(self,rollno,grade,percentage):
        self.rollno=rollno
        self.grade=grade
        self.percentage=percentage
    def putDataStudent(self):
        print("Roll No:",self.rollno)
        print("Grade:",self.grade)
        print("Percentage:",self.percentage)
        print("*"*40)

class Teacher(Person):
    def getDataTeacher(self,subject,salary,experience):
        self.subject=subject
        self.salary=salary
        self.experience=experience
    def putDataTeacher(self):
        print("Subject:",self.subject)
        print("Salary:",self.salary)
        print("Experience:",self.experience)

student1=Student()
print("Student Details")
student1.getDataGeneral("Jay",18,"Male",2594)
student1.getDataStudent(25,"A","80%")
student1.putDataGeneral()
student1.putDataStudent()

teacher1=Teacher()
print("Teacher Details")
teacher1.getDataGeneral("Jigar Sir",40,"Male",6789)
teacher1.getDataTeacher("Maths",6000,"8 Years")
teacher1.putDataGeneral()
teacher1.putDataTeacher()

