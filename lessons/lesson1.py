class Kaka:
    # Конструктор класса
    def __init__(self, name, hp, lvl):
        # Атрибуты
        self.name_hero = name
        self.hp_hero = hp
        self.lvl_hero = lvl
    # Объект класса
    def action(self):
        return f"{self.name_hero}Hero base action"


#Объкт/ Экземпляр на основе класса
kirito = Kaka('Kirito', 1000, 100)
asuna = Kaka('asuna', 1000, 100)

asuna.hp_hero += 200
kirito.lvl_hero -= 22
print(asuna.hp_hero,kirito.lvl_hero)
print()