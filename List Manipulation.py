#Write a Python function that 
# returns employees whose salary is greater than 5,000,
#  sorted by salary in descending order.
employees = [
    {"name": "John", "salary": 4000},
    {"name": "Alice", "salary": 7000},
    {"name": "Mark", "salary": 6000},
    {"name": "Sarah", "salary": 3000},
]
def filter_sort_employees(employees):
    filtered_employees=[emp for emp in employees if emp["salary"] > 5000]
    sorted_employees=sorted(filtered_employees, key=lambda x: x["salary"], reverse=True)
    return sorted_employees  
print(filter_sort_employees(employees))
# i used lambda function as to oppose to using function  because it is 
# more concise
# allows for inline sorting without the need to define a separate function.
# Makes the code cleaner and easier to read, especially for simple operations like sorting by a specific key.

#Using a separate function for sorting can 
# be beneficial when the sorting logic is more 
# complex or needs to be reused in multiple places. It can improve code organization and maintainability, especially in larger projects where functions can be tested and documented independently.
def get_salary(emp):
    return emp["salary"]

def filter_sort_employees(employees):
    filtered_employees = [
        emp for emp in employees if emp["salary"] > 5000
    ]

    sorted_employees = sorted(
        filtered_employees,
        key=get_salary,
        reverse=True
    )

    return sorted_employees

print(filter_sort_employees(employees))