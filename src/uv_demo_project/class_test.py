class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    def display_info(self):
	    print(f'Model: {self.model}, Color: {self.color}')
car1 = Car("Toyota", "Red")
car1.display_info()  # 输出: Model: Toyota, Color: Red

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def display_info(self):
        print(f'Name: {self.name}, Salary: {self.salary}')
