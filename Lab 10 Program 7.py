import pickle
employee = {"empcode": 123, "empname": "John Doe", "Date of Joining": "2023-01-01", "Salary": 50000}
with open("employee.pkl", "wb") as file:
    pickle.dump(employee, file)
with open("employee.pkl", "rb") as file:
    deserialized_employee = pickle.load(file)
print(deserialized_employee)
