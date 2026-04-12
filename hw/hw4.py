rates = {
    "KGS":1,
    "USD":87.5,
    "EUR":100,
    "RUB":1.2
}


class Money:
    def __init__(self,amount,currency):
        self.amount = amount
        self.currency = currency

    def convert_to_kgs(self):
        return self.amount * rates[self.currency]

    def __add__(self, other):
        total = self.convert_to_kgs() + other.convert_to_kgs()
        return Money(total, "KGS")

    def __sub__(self, other):
        total = self.convert_to_kgs() - other.convert_to_kgs()
        return Money(total, "KGS")

    def __mul__(self, number):
        return Money(self.amount * number, self.currency)

    def __truediv__(self, number):
        return Money(self.amount / number, self.currency)

    def __str__(self):
        return str(self.amount) + " " + self.currency

money1 = Money(153, "USD")
money2 = Money(7777, "KGS")

print(money1 + money2)
print(money1 - money2)
print(money1 * 2)
print(money2 / 2)





