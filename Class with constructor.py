class Student:
    studentcount=0
    def __init__(self,rino,name):
        self.rino=rino
        self.name=name
        Student.studentcount++1;
    def displayStudent(self):
            print("roll no:",self.rino)
            print("name:",self.name)
            #studentcount=studentcount+1

stud1=Student(10,"ALL")
stud2=Student(11,"fvb")
stud1.displayStudent()
stud2.displayStudent()
print("total no of students",Student.studentcount)
