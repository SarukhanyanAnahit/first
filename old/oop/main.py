from manager import Manager
from employee import Employee

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

print(employee3)
print(second_manager)

first_manager.remove()