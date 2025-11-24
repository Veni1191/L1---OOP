class Student:
    def __init__(self):
        self.name = ""
        self.year = ""
    
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
        self.year = input("Enter your year level: ")
        self.m1 = int(input("Enter mark for 1st subject: "))
        self.m2 = int(input("Enter mark for 2nd subject: "))
        self.m3 = int(input("Enter mark for 3rd subject: "))
        
    def show_details(self):
        self.total = self.m1 + self.m2 + self.m3
        self.average = self.total/3
        print("The report card details are:")
        print(f"The student's name is: {self.name}")
        print(f"The year level of {self.name} is: {self.year}")
        print(f"The total marks of {self.name}: {self.total}")
        print(f"Average for {self.name} is: {self.average}")
        if self.average >= 90:
            print("Grade:A")
        elif self.average >= 70:
            print("Grade:B")
        elif self.average >= 55:
            print("Grade:C")
        elif self.average >=30:
            print("Grade:D")
        else:
            print("Grade:FAIL")
    
student1 = Report()
student1.input_info()
student1.show_details()



        