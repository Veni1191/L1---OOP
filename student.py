#creating the parent class
class Student:
    #making constructor method
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #making method
    def details(self):
        print("The student details are:")
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")


#creating the child class
class School(Student):
    def __init__(self, name, age,grade,house_team):
        super().__init__(name, age)
        self.grade = grade
        self.house_team = house_team
    
    #making another method
    def information(self):
        print(f"Grade:{self.grade}")
        print(f"House Team: {self.house_team}")

student1 = School("Venisha",13,7,"Pari-Blue")
student1.details()
student1.information()

    



