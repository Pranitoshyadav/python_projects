class student:
    def greet(self):
        print("Hello students")

s = student()
s.greet()

class student:
    def __init__(self, name):
        self.name = name
        print("student creted")

s = student("Riya")

class student:
    def __init__(self):
        print("student creted")

    def __del__(self):
        print("student deleted")

s = student()
del s

fruits = ["Apple", "Banana","Mango"]

for index, fruits in enumerate(fruits):
    print(index, fruits)