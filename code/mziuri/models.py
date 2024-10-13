
class Member:
    
    def __init__(self, name,age , status, subject):
        self.name = name 
        self.age = age

        self.status = status
        self.subject = subject

class Teacher(Member):

    def __init__(self, name, age , status, subject, salary ):

        super().__init__(name, age , status, subject)
        self.salary = salary

    def calculate_yearly_salary(self):
        return self.salary * 12
        



class Students(Member):

    def __init__(self, name,age, status, grade ):
        super().__init__(name, age, status)
        self.grade = grade
    
    def __str__(self):
        return f"name: {self.name}, age:{self.age}, status :{self.status}, grade :{self.grade}"




lizi = Students("lizi", 14, "student" , 99.5)
shotiko = Teacher("shotiko", 21, "theacher", "python", 10000)

print(Teacher.calculate_yearly_salary(shotiko))
print(lizi.__str__())