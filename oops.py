class Student :
    school = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name : ", self.name)
        print("age : ", self.age)
        print("school : ", self.school)

s1 = Student("Rahul", 15)
s2 = Student("Priya", 14)

s1.display()
print()

s2.display()



class student():
    grade = 10
    print("Hi I am a student from ", grade)

ob = student()