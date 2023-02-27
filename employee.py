import json

class Employee:
    def __init__(self, name, employee_id) -> None:
        self.name = name
        self.employee_id = employee_id

employee = Employee("John Smith", 40)

def f(x):
    return x.__dict__

json_data1 = json.dumps(employee, default=f)
print(json_data1)