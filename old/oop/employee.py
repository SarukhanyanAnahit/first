from human import Human

class Employee(Human):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self._manager = None

    @property
    def manager(self):
        return self._manager

    @manager.setter
    def manager(self, value):
        self._manager = value

    def __str__(self):
        return f"employee: {self.name} {self.surname}, age: {self.age}"
