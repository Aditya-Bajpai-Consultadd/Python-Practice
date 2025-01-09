#Create a class hierarchy for employees, with a base class and
#subclasses for full-time, part-time, and contractor employees.
#Include shared attributes like name, ID, and salary calculation in
#the base class. Each subclass should calculate the salary based
#on its type (full-time, part-time, contractor). Apply tax deductions
#(e.g., 10%) and Provident Fund (PF) deductions (e.g., 12%) for
#full-time and part-time employees. For contractors, apply only the
#tax deduction and no PF. The final salary after deductions should
#be returned for each employee type.

class Employee:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, ID, salary):
        super().__init__(name, ID)
        self.salary = salary

    def calculate_salary(self):
        return self.salary - (0.10 * self.salary) - (0.12 * self.salary)
    
class PartTimeEmployee(Employee):
    def __init__(self, name, ID, salary):
        super().__init__(name, ID)
        self.salary = salary

    def calculate_salary(self):
        return self.salary - (0.10 * self.salary) - (0.12 * self.salary)
    
class Contractor(Employee):
    def __init__(self, name, ID, salary):
        super().__init__(name, ID)
        self.salary = salary

    def calculate_salary(self):
        return self.salary - (0.10 * self.salary)
    
full_time_employee = FullTimeEmployee("John", 1, 1000)
part_time_employee = PartTimeEmployee("Jane", 2, 500)
contractor = Contractor("Jack", 3, 100)

print(full_time_employee.calculate_salary())
print(part_time_employee.calculate_salary())
print(contractor.calculate_salary())
