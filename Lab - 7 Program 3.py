company_data = {
    "D01": [(101, 50000), (102, 60000), (103, 55000)],
    "D02": [(201, 45000), (202, 70000), (203, 48000)],
    "D03": [(301, 65000), (302, 62000)]
}
for dept, employees in company_data.items():
    salaries = [salary for _, salary in employees]
    min_salary = min(salaries)
    max_salary = max(salaries)
    
print(f"Department {dept}:")
print("  Minimum Salary:", min_salary)
print("  Maximum Salary:", max_salary)
