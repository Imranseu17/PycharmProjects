__author__='Fahim Shahriyar'

from Dir1 import file_01 as F

print F.Sum(14,2)   

class Student(object):
    def __init__(self,name="",ID=""):
        self.name=name
        self.Id=ID
        self.__cgpa=2.5

    def printNamne(self):
        print self.name

    def printId(self):
        print self.Id

    def getCgpa(self):
        return self.__cgpa

    def study(self):
        pass

class Parent:
    ##def __init__(self):
        pass

class JongiStudent(Student):

    ##def __init__(self,name, Id):
      ##  self.brainWashStatus = False

    def doTerrorism(self):
        print "Bombing"

    def study(self):
        print "Missing Classes For 10 Days"

student_1 = JongiStudent("Intiser","200102343")
print student_1.name, student_1.Id, student_1.getCgpa()

student_1.study()

student_1.doTerrorism()