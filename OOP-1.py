from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary
    @property
    def name(self):
        return self.__name
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,new_salary):
        if new_salary >= 3000:
            self.__salary = new_salary
    def __str__(self,new_salary):
        if new_salary <= 3000:
            return f"Name: {self.__name}, salary:{self.__salary}"
class Developer(Employee):
    def __init__(self, name, salary,language):
        super().__init__(name, salary)
        self.__language = language
    @property
    def language(self):
        return self.__language 
    def __str__(self):
        return f"Developer: {self.name}, salary:{self.salary}, Language: {self.__language}"
    
class Manager(Employee):
    def __init__(self, name, salary,team_size):
        super().__init__(name, salary)
        self.__team_size = team_size
    @property
    def team_size(self):
        return self.__team_size 
    def __str__(self):
        return f"Manager: {self.name}, salary:{self.salary}, Team size: {self.__team_size}"
    

employees = [
    Developer("Ahmed", 10000, "Python"),
    Manager("Mohamed", 15000, 10),
    Developer("Ali", 8000, "Java")
]
for employee in employees:
    print(employee)



        