class Human():
    def __init__(self, n, s, a):
        self.__name = n
        self.__surname = s
        self.__age = a

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

class Employee(Human):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.__manager = None

    def set_manager(self, manager):
        self.__manager = manager

    def get_manager(self):
        return self.__manager

class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.__employees = []

    def hire(self, employee):
        if employee.get_manager() is not None:
            print(f"{employee.get_name()} is already hired by another manager.")
            return

        if len(self.__employees) >= 10:
            print(f"{employee.get_name()} can't be hired: max 10 employees reached.")
            return

        self.__employees.append(employee)
        employee.set_manager(self)
        print(f"{employee.get_name()}, {employee.get_surname()} hired by {self.get_name()}")

    def fire(self, employee):
        if employee in self.__employees:
            self.__employees.remove(employee)
            employee.set_manager(None)
            print(f"{employee.get_name()}, {employee.get_surname()} was fired by {self.get_name()}")
        else:
            print(f"{employee.get_name()}, {employee.get_surname()} is not an employee of {self.get_name()}")

first_manager = Manager("Vardanyan", "Ani", 40)
second_manager = Manager("Hakobyan", "Arshak", 38)

employee1 = Employee("Janna", "Hakobyan", 25)
employee2 = Employee("Larisa", "Hovhannisyan", 28)
employee3 = Employee("Armine", "Davtyan", 35)

first_manager.hire(employee1)
second_manager.hire(employee2)
second_manager.hire(employee1)
first_manager.fire(employee1)
first_manager.fire(employee2)
second_manager.hire(employee1)
