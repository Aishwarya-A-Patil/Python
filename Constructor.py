#Constructor
class Employee:
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def empDetails(self):
        print("Employee Name: ", self.name)
        print("Employee Age: ", self.age)
        print("Employee Salary: ", self.salary)
        print("Employee Gender: ", self.gender)

#When constructor is defined and used , we pass arguments at class initialization
emp = Employee("Aishwarya", 28, 10000, "Female")
emp.empDetails()