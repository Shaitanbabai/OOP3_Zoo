import pandas as pd


class Animal:
    """Базовый класс для представления животных."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Метод make_sound() должен быть реализован в дочерних классах.")

    def eat(self):
        raise NotImplementedError("Метод eat() должен быть реализован в дочерних классах.")


class Bird(Animal):
    """Класс, представляющий птиц."""

    def __init__(self, name, age, feathers_color):
        super().__init__(name, age)
        self.feathers_color = feathers_color

    def make_sound(self):
        print(f"{self.name} поет: чирик-чирик!")

    def eat(self):
        print(f"{self.name} клюет семена.")


class Mammal(Animal):
    """Класс, представляющий млекопитающих."""

    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} издает звук: ррр!")

    def eat(self):
        print(f"{self.name} ест мясо или траву.")


class Reptile(Animal):
    """Класс, представляющий рептилий."""

    def __init__(self, name, age, scales_color):
        super().__init__(name, age)
        self.scales_color = scales_color

    def make_sound(self):
        print(f"{self.name} шипит: шшш!")

    def eat(self):
        print(f"{self.name} ест насекомых или мелких животных.")


class ZooKeeper:
    """Класс, представляющий смотрителя зоопарка."""

    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")


class Veterinarian:
    """Класс, представляющий ветеринара."""

    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")


class Zoo:
    """Класс, представляющий зоопарк."""

    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def get_animal_by_name(self, name):
        for animal in self.animals:
            if animal.name == name:
                return animal
        return None

    def get_staff_by_position(self, position):
        for staff_member in self.staff:
            if isinstance(staff_member, type(position)):
                return staff_member
        return None

    def save_to_file(self, filename):
        animals_data = []
        for animal in self.animals:
            if isinstance(animal, Bird):
                animals_data.append(["Bird", animal.name, animal.age, animal.feathers_color])
            elif isinstance(animal, Mammal):
                animals_data.append(["Mammal", animal.name, animal.age, animal.fur_color])
            elif isinstance(animal, Reptile):
                animals_data.append(["Reptile", animal.name, animal.age, animal.scales_color])

        staff_data = []
        for staff_member in self.staff:
            if isinstance(staff_member, ZooKeeper):
                staff_data.append(["ZooKeeper", staff_member.name, staff_member.experience])
            elif isinstance(staff_member, Veterinarian):
                staff_data.append(["Veterinarian", staff_member.name, staff_member.specialization])

        animals_df = pd.DataFrame(animals_data, columns=["Type", "Name", "Age", "Color"])
        staff_df = pd.DataFrame(staff_data, columns=["Position", "Name", "Details"])
