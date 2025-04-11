from datetime import datetime

class Animal:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def list_commands(self):
        return self.commands

class DomesticAnimal(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.type = "domestic"

class PackAnimal(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.type = "pack"

# Домашние животные
class Dog(DomesticAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.species = "dog"

class Cat(DomesticAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.species = "cat"

class Hamster(DomesticAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.species = "hamster"

# Вьючные животные
class Horse(PackAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.species = "horse"

class Camel(PackAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.species = "camel"

class Donkey(PackAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.species = "donkey"