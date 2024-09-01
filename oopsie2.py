import random

class Sorter:
    guild = ["master", "caster", "assassin", "scout", "warrior"]
    # def __init__(self):
    #     self.guild = ["master", "caster", "assassin", "scout", "warrior"]
    @classmethod
    def sort(cls, name):
        guild = random.choice(cls.guild)
        print(f"{name} is from {guild} guild!")

# st = Sorter()
Sorter.sort("gabe")    