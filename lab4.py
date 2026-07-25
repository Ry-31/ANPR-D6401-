class Teacher:
    def display(self):
        print("I am a Teacher")


class Student:
    def display(self):
        print("I am a Student")


class TeachingAssistant(Teacher, Student):
    pass


obj = TeachingAssistant()

obj.display()
Teacher.display(obj)
Student.display(obj)

    