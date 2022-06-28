class Student:
    college = 'RIT' 

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self): #instance methods
        return (self.m1 + self.m2 + self.m3)/3
    
    @classmethod
    def getSchool(cls):
        return cls.college

    @staticmethod
    def info():
        print("Module name: ",__name__)


s1 = Student(38,59,23)
s2 = Student(43,65,23)

print(s1.avg())
print(s2.getSchool())

s1.info()
Student.info()
