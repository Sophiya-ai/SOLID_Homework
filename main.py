from abc import ABC, abstractmethod

class Fighter():
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def game(self,monster):
        self.weapon.attack(self,monster)

    def change_weapon(self,new_weapon):
        self.weapon = new_weapon
        print(f"{self.upper()} поменял оружие на {self.weapon.upper()}")

    def overshoot(self):
        print(f"{self.upper()} промахнулся")

    def hit(self):
        print(f"{self.upper()} попал")

class Monster():
    def __init__(self, name):
        self.name = name

    def die(self):
        print(f"{self.upper()} умер!")

    def run(self):
        print(f"{self.upper()} убежал!")

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def __init__(self, name):
        self.name = name

    def attack(self, fighter, monster):
        print(f"{fighter.upper()} протыкает монстра {monster.upper()} мечом")

class Bow(Weapon):
    def __init__(self, name):
        self.name = name
        
    def attack(self, fighter, monster):
        print(f"{fighter.upper()} выстреливает в монстра {monster.upper()} из лука")

escalibur = Sword()
firedSword = Sword()
wighteBow = Bow()
blackBow = Bow()
Bill = Fighter(escalibur)
Alien = Monster()
Bill.game(Alien)
Alien.die()
Bill.change_weapon(blackBow)
Bill.game(Alien)
Bill.overshoot()
Alien.run()

