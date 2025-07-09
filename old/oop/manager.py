from employee import Employee

class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self._employees = []

    def hire(self, employee):
        if employee.manager is not None:
            print(f"{employee.name} is already hired")
            return

        if len(self._employees) >= 10:
            print(f"{employee.name} can't be hired: max 10 employees reached")
            return

        self._employees.append(employee)
        employee.manager = self
        print(f"{employee.name}, {employee.surname} hired by {self.name}")

    def fire(self, employee):
        if employee in self._employees:
            self._employees.remove(employee)
            employee.manager = None
            print(f"{employee.name}, {employee.surname} was fired by {self.name}")
        else:
            print(f"{employee.name}, {employee.surname} is not an employee of {self.name}")

    def remove(self):
        for emp in self._employees:
            emp.manager = None
        self._employees=[]
        print(f"manager {self.name} was removed")

    def __str__(self):
        return f"manager: {self.name} {self.surname}, age: {self.age}, employees: {len(self._employees)}"
