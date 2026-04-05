class Hero:
    def __init__(self, name, lvl, hp, strength):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.strength = strength

    def greet(self):
        print(f"Привет Я {self.name}")

    def attack(self):
            print(f"{self.name} наносить удар!")

    def rest(self):
            print(f"{self.name}  отдыхает и восстанавливает здоровье...")


class Type(Hero):
    def __init__(self, name, lvl, hp, strength):
        super().__init__(name,lvl,hp,strength)


    def warrior(self, stamina):
        self.stamina = stamina
        print(f"{self.name} атакует мечом!")



    def mage(self, name):
        self.mana = name
        print(f"{self.name} кастует заклинание!")


    def assassin(self, stealth):
        self.stealth = stealth
        print(f"{self.stealth} атакует из-под тишка")


Warrior = Type("Kalys", 100, 100,99)
Mage = Type("Chuke",100, 100,90)
Assassin = Type("Altyke",90, 100,99)

random = input(f"Выберите героя: Warrior/Mage/Assassin")