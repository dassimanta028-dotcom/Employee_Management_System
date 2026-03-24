import json
import os

FILE_NAME = "employee.json"

# ------------ Class ---------------------
class Employee:
    def __init__(self, eid, name, age, department, salary):
        self.eid = eid
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def to_dict(self):
        return {
            "eid": self.eid,
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "salary": self.salary
        }

# ------------ File Handling -----------------
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# ------------ Functions ----------------
def add_employee():
    try:
        eid = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        department = input("Enter department: ")
        salary = float(input("Enter salary: "))

        employee = Employee(eid, name, age, department, salary)

        data = load_data()

        # check duplicate ID
        for emp in data:
            if emp['eid'] == eid:
                print("Employee ID already exists!")
                return

        data.append(employee.to_dict())
        save_data(data)

        print("Employee added successfully!")

    except ValueError:
        print("Invalid input! Please enter correct data.")

def view_employee():
    data = load_data()
    if not data:
        print("No employee data found.")
        return

    for emp in data:
        print("\n--------------------")
        print(f"ID: {emp['eid']}")
        print(f"Name: {emp['name']}")
        print(f"Age: {emp['age']}")
        print(f"Department: {emp['department']}")
        print(f"Salary: {emp['salary']}")

def search_employee():
    try:
        eid = int(input("Enter employee ID: "))
        data = load_data()

        for emp in data:
            if emp['eid'] == eid:
                print("\nEmployee Found:")
                print(emp)
                return

        print("Employee not found.")

    except ValueError:
        print("Invalid input!")

def update_employee():
    try:
        eid = int(input("Enter employee ID: "))
        data = load_data()

        for emp in data:
            if emp['eid'] == eid:
                emp['name'] = input("Enter new name: ")
                emp['age'] = int(input("Enter new age: "))
                emp['department'] = input("Enter new department: ")
                emp['salary'] = float(input("Enter new salary: "))

                save_data(data)
                print("Employee updated successfully!")
                return

        print("Employee not found.")

    except ValueError:
        print("Invalid input!")

def delete_employee():
    try:
        eid = int(input("Enter employee ID: "))
        data = load_data()

        new_data = [emp for emp in data if emp['eid'] != eid]

        if len(data) == len(new_data):
            print("Employee not found!")
        else:
            save_data(new_data)
            print("Employee deleted successfully!")

    except ValueError:
        print("Invalid input!")

# ------------ Menu ----------------
def menu():
    while True:
        print("\n============= Employee Management System =============")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_employee()
            elif choice == 2:
                view_employee()
            elif choice == 3:
                search_employee()
            elif choice == 4:
                update_employee()
            elif choice == 5:
                delete_employee()
            elif choice == 6:
                print("Thank you for using this program!")
                break
            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number!")

# ------------ Run Program ----------------
if __name__ == "__main__":
    menu()