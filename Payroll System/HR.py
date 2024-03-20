class PayrollSystem:
    def get_salary(self, employees):
        print("****** Payroll ******")
        for emp in employees:
            print(f"Name: {emp.name}, ID: {emp.id}")
            print(f"Salary: {emp.get_salary()}\n")
            print(f"CTC: {emp}")

class Employee:
    def __init__(self, id, name):
        self. id = id
        self.name = name

class MonthlySalary(Employee):
    def __init__(self, id, name, monthly_salary):
        super().__init__(id, name)
        self.monthly_salary = monthly_salary

    def get_salary(self):
        return self.monthly_salary
    
    def get_ctc(self):
        return 12 * self.monthly_salary

class HourlySalary(Employee):
    def __init__(self, id, name, hour_worked, hourly_rate):
        super().__init__(id, name)
        self.hour_worked = hour_worked
        self.hourly_rate = hourly_rate
    
    def get_salary(self):
        return self.hour_worked * self.hourly_rate
    
    def 

class ComissionSalary(MonthlySalary):
    def __init__(self, id, name, monthly_salary, comission):
        super().__init__(id, name, monthly_salary)
        self.comission = comission

    def get_salary(self):
        base_salary = super().get_salary()
        return self.comission + base_salary
    
    def get_ctc(self):
