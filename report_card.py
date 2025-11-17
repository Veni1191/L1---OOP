class Student:
    def __init__(self):
        self.name = ""
        self.grade = ""
    
class Report(Student):
    def __init__(self):
        super().__init__()
        self.m1 = 0
        self.m2 = 0
        self.m3 = 0
        self.total = 0
        self.average = 0

    def input_info(self):    
        self.name = input("Enter your name: ")
        self.grade = input("Enter your grade: ")
        self.m1 = int(input("Enter mark for 1st subject: "))
        self.m2 = int(input("Enter mark for 2nd subject: "))
        self.m3 = int(input("Enter mark for 3rd subject: "))
        
       
        