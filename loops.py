class Student:

    pincode = '500018'
    rank  = 'A'
    name = "Dinesh"


    def __init__(self,name,age):
        self.name = name
        self.age = age


    def stdname(self):
        return f'student name is {self.name}'

    def stdage(self):
        print('student age is {self.age}')

    @classmethod
    def stdpin(cls):
        return f'location of student is {cls.pincode}'

    
    def studentdetails(location):
        return f'student info {location}'

    @staticmethod
    def callnaem(name): # its not self nither @classsmen
        return f"{name}"
    
    def studentinfo(self,location):
        return f'{self.name},{self.age},{self.studentdetails(location)}'




s = Student(name='pavan',age=25)
print(s.pincode)
print(s.stdpin())
print(s.callnaem("dsafasf"))