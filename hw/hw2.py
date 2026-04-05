import random

class Hero:
    def __init__(self, name, lvl, hp, strength):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.strength = strength

    def greet(self):
        print(f"Привет Я {self.name}")

    def attack(self):
        print(f"{self.name} наносит удар!")

    def rest(self):
        print(f"{self.name} отдыхает...")


class Warrior(Hero):
    def __init__(self, name, lvl, hp, strength, stamina):
        super().__init__(name, lvl, hp, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name} атакует мечом!")


class Mage(Hero):
    def __init__(self, name, lvl, hp, strength, mana):
        super().__init__(name, lvl, hp, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name} кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, lvl, hp, strength, stealth):
        super().__init__(name, lvl, hp, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name} атакует из-под тишка!")


warrior = Warrior("Kalys", 100, 100, 99, 50)
mage = Mage("Chuke", 100, 100, 90, 100)
assassin = Assassin("Altyke", 90, 100, 99, 80)

print("Выберите героя: warrior / mage / assassin")
choice = input().lower()

if choice == "warrior":
    player = warrior
elif choice == "mage":
    player = mage
elif choice == "assassin":
    player = assassin
else:
    print("Ошибка")
    exit()

enemy = random.choice([warrior, mage, assassin])

print("Ты:", player.name)
print("Враг:", enemy.name)

if player == enemy:
    print("Ничья")
elif (player == warrior and enemy == assassin) or \
     (player == assassin and enemy == mage) or \
     (player == mage and enemy == warrior):
    print("Ты выиграл!")
else:
    print("Ты проиграл!")