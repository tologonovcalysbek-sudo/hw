from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self,name,level,health,strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print (f"Привет,я {self.name}, мой уровень  {self.level}")

    def rest(self):
        print (f"{self.name} отдыхает ")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass



class Warrior(Hero):
    def attack(self):
        print(f"Воин атакует мечом")

class Mage(Hero):
    def attack(self):
        print(f"Маг изпользует магию")

class Assassin(Hero):
    def attack(self):
        print(f"Ассасин атакует из под тишка")

warrior = Warrior('Kalys',77,100,100)
mage = Mage('Chuke',77,100,90)
assassin = Assassin('Altyke',78,100,92)


warrior.greet()
warrior.rest()
warrior.attack()

mage.greet()
mage.rest()
mage.attack()

assassin.greet()
assassin.rest()
assassin.attack()


