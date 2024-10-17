from abc import ABC, abstractmethod

class Fighter():
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def game(self, monster):
        print(f"Боец {f.name.upper()} в игре и видит монстра {monster}!")
        self.weapon.attack()

    def change_weapon(self,new_weapon):
        self.weapon = new_weapon
        print(f"{self.name.upper()} поменял оружие на {self.weapon.name.upper()}")

    def overshoot(self):
        print(f"{self.name.upper()} промахнулся")

    def hit(self):
        print(f"{self.name.upper()} попал")

class Monster():
    def __init__(self, name):
        self.name = name

    def die(self):
        print(f"{self.name.upper()} умер!")

    def run(self):
        print(f"{self.name.upper()} убежал!")

class Weapon(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def __init__(self, name):
        super().__init__(name)

    def attack(self):
        print(f"Боец протыкает монстра мечом - {self.name.upper()}!")

class Bow(Weapon):
    def __init__(self, name):
        super().__init__(name)

    def attack(self):
        print(f"Боец выстреливает в монстра из лука - {self.name.upper()}...")

s = Sword("эскалибур")
b1 = Bow("черный лук")
b2 = Bow("белый лук")
f = Fighter("Ваня",s)
m1 = Monster("Чужой")
m2 = Monster("хищник")
f.game(m1.name.upper())
m1.die()
f.change_weapon(b1)
f.game(m2.name.upper())
f.overshoot()
m2.run()
f.change_weapon(b2)
f.game(m2.name.upper())
f.hit()
m2.die()

