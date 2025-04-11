from animal_classes import Dog, Cat, Hamster, Horse, Camel, Donkey
from counter import Counter
from datetime import datetime
import sys


class AnimalRegistry:
    def __init__(self):
        self.animals = []
        self.counter = Counter()

    def add_animal(self):
        """Добавление нового животного"""
        with self.counter as counter:
            try:
                print("\nДоступные виды животных:")
                print("1. Собака")
                print("2. Кошка")
                print("3. Хомяк")
                print("4. Лошадь")
                print("5. Верблюд")
                print("6. Осел")

                choice = input("Выберите вид животного (1-6): ")
                name = input("Введите имя животного: ")
                birth_date = input("Введите дату рождения (ГГГГ-ММ-ДД): ")

                birth_date = datetime.strptime(birth_date, '%Y-%m-%d')

                animal = None
                if choice == '1':
                    animal = Dog(name, birth_date)
                elif choice == '2':
                    animal = Cat(name, birth_date)
                elif choice == '3':
                    animal = Hamster(name, birth_date)
                elif choice == '4':
                    animal = Horse(name, birth_date)
                elif choice == '5':
                    animal = Camel(name, birth_date)
                elif choice == '6':
                    animal = Donkey(name, birth_date)

                if animal:
                    self.animals.append(animal)
                    counter.add()
                    print(f"\nЖивотное {name} успешно добавлено!")
                    return True
                return False
            except ValueError:
                print("Ошибка: Неверный формат даты!")
                return False

    def list_animals(self):
        """Просмотр списка животных"""
        if not self.animals:
            print("\nРеестр пуст!")
            return

        print("\nСписок животных:")
        for i, animal in enumerate(self.animals, 1):
            print(f"{i}. {animal.species.capitalize()} - {animal.name}")

    def show_commands(self):
        """Просмотр команд животного"""
        self.list_animals()
        try:
            choice = int(input("\nВыберите номер животного: ")) - 1
            animal = self.animals[choice]
            commands = animal.list_commands()
            if commands:
                print(f"\nКоманды, которые знает {animal.name}:")
                for cmd in commands:
                    print(f"- {cmd}")
            else:
                print(f"\n{animal.name} пока не знает команд!")
        except (ValueError, IndexError):
            print("\nОшибка: Неверный выбор!")

    def teach_command(self):
        """Обучение животного новой команде"""
        self.list_animals()
        try:
            choice = int(input("\nВыберите номер животного: ")) - 1
            animal = self.animals[choice]
            command = input("Введите новую команду: ")
            animal.add_command(command)
            print(f"\n{animal.name} успешно обучен команде '{command}'!")
        except (ValueError, IndexError):
            print("\nОшибка: Неверный выбор!")

    def run(self):
        """Главное меню программы"""
        while True:
            print("\n=== Реестр домашних животных ===")
            print("1. Завести новое животное")
            print("2. Показать список животных")
            print("3. Показать команды животного")
            print("4. Обучить животное новой команде")
            print("5. Выйти")

            choice = input("\nВыберите действие (1-5): ")

            if choice == '1':
                self.add_animal()
            elif choice == '2':
                self.list_animals()
            elif choice == '3':
                self.show_commands()
            elif choice == '4':
                self.teach_command()
            elif choice == '5':
                print("\nДо свидания!")
                sys.exit()
            else:
                print("\nНеверный выбор!")


if __name__ == "__main__":
    registry = AnimalRegistry()
    registry.run()