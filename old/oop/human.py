from abc import ABC, abstractmethod

class Human(ABC):
    def __init__(self, n, s, a):
        self._name = n
        self._surname = s
        self._age = a

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @abstractmethod
    def __str__(self):
        pass
