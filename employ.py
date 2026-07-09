class person :
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


class employ(person):
    def __init__(self, name, idnmber, salary, post):
        self.salary = salary
        self.post = post

        super().__init__(name, idnmber)


a = employ('Rahul', 886012, 200000, "Intern")
a.display()