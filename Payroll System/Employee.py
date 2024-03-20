import HR

Employee_Monthly_salary = HR.MonthlySalary(123, 'Lucky Kumar', 250000)
Employee_Hourly_salary = HR.HourlySalary(234, 'Vivian Pal', 1200, 30)
Employee_Commision_salary = HR.ComissionSalary(456, 'Sweshik', 1000, 240)
Employee_CTC_Monthly = HR.CTC_Monthly()

payroll_system = HR.PayrollSystem(123, 'Lucky Kumar', 250000)

payroll_system.get_salary([
    Employee_Monthly_salary,
    Employee_Hourly_salary,
    Employee_Commision_salary
])