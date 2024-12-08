class Student:
    def __init__(self, name, studentId, gpa):
        self.name = name
        self.studentId = studentId
        self.gpa = gpa

    def printStudentDetails(self):
        print(f"Студент: {self.name}, ID: {self.studentId}, GPA: {self.gpa}")


student = Student("First student", 1, 4.3)
student.printStudentDetails()
