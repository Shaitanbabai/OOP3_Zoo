class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):

    def __init__(self, name, age, feathers_color):
        super().__init__(name, age)
        self.feathers_color = feathers_color

    def make_sound(self):
        print(f"{self.name} поет: чирик-чирик!")

    def eat(self):
        print(f"{self.name} клюет семена.")


class Mammal(Animal):

    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} издает звук: ррр!")

    def eat(self):
        print(f"{self.name} ест мясо или траву.")


class Reptile(Animal):

    def __init__(self, name, age, scales_color):
        super().__init__(name, age)
        self.scales_color = scales_color

    def make_sound(self):
        print(f"{self.name} шипит: шшш!")

    def eat(self):
        print(f"{self.name} ест насекомых или мелких животных.")


class ZooKeeper:

    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")


class Veterinarian:

    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")


class Zoo:

    def __init__(self, name, creatures, personnel):
        self.name = name
        self.animals = creatures
        self.staff = personnel

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)


animals = [
    Bird("Воробей", 2, "коричневый"),
    Mammal("Собака", 4, "рыжий"),
    Reptile("Змея", 3, "зеленый"),
]

staff = [
    ZooKeeper("Иван", 10),
    Veterinarian("Мария", "хищные птицы"),
]

zoo = Zoo("Центральный зоопарк", animals, staff)

# Добавить новое животное
zoo.add_animal(Bird("Попугай", 1, "пестрый"))

# Добавить нового сотрудника
zoo.add_staff(ZooKeeper("Петр", 5))

# Смотритель кормит животное
zoo.staff[0].feed_animal(zoo.animals[0])

# Ветеринар лечит животное
zoo.staff[1].heal_animal(zoo.animals[2])
