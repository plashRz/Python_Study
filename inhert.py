class Family:
    def __init__(self, name):
        if not name:
            raise ValueError("Name must be specified")
        else:
            self.name = name

class inheritThis(Family):
    def __init__(self, money, land, name):
        super().__init__(name)
        self.money = money
        self.land = land
    def __str__(self):
        return f"Name: {self.name}\nLand: {self.land}\nMoney: {self.money}"    

class DueThat(Family):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount
        
    def __str__(self):
        if self.amount == 0:
            return "No Dues Remaining"
        return f"Name: {self.name}\nAmount: {self.amount}"

    def remainingAssets(self, obj):
        if obj.name is self.name:
            obj.money = obj.money - self.amount
            self.amount = 0    

iht = inheritThis(1000000, 2160, "Avery")
dt = DueThat(f"{iht.name}", 578340)

print(iht, dt, sep="\n=================\n")
dt.remainingAssets(iht)
print("After dust is settled!")
print(iht, dt, sep="\n=================\n")