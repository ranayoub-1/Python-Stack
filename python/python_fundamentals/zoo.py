class Animal:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.health = 100
        self.happiness = 100

    def display_info(self):
        print(f"Name: {self.name}, Health: {self.health}, Happiness: {self.happiness}")

    def feed(self):
        self.health += 10
        self.happiness += 10
        return self


class Lion(Animal):
    def __init__(self, name, age=0):
        super().__init__(name, age)
        self.mane_size = "Large"

    def display_info(self):
        print("Type: Lion")
        super().display_info()
        print("-" * 30)

    def feed(self):
        self.health += 15
        self.happiness += 5
        return self


class Tiger(Animal):
    def __init__(self, name, age=0):
        super().__init__(name, age)
        self.stripe_count = 50

    def display_info(self):
        print("Type: Tiger")
        super().display_info()
        print("-" * 30)

    def feed(self):
        self.health += 5
        self.happiness += 15
        return self


class Monkey(Animal):
    def __init__(self, name, age=0):
        super().__init__(name, age)
        self.energy = 100

    def display_info(self):
        print("Type: Monkey")
        super().display_info()
        print("-" * 30)

    def feed(self):
        self.health += 8
        self.happiness += 20
        return self


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animals.append(Lion(name))

    def add_tiger(self, name):
        self.animals.append(Tiger(name))

    def add_monkey(self, name):
        self.animals.append(Monkey(name))

    def print_all_info(self):
        print("=" * 40)
        print(self.name)
        print("=" * 40)
        for animal in self.animals:
            animal.display_info()


# تشغيل البرنامج
zoo1 = Zoo("John's Zoo")

zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.add_monkey("George")

print("Before feeding:")
zoo1.print_all_info()

#  هنا استدعاء feed()
for animal in zoo1.animals:
    animal.feed()

print("\nAfter feeding:")
zoo1.print_all_info()