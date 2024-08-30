class Wizard:
    def __init__(self, name, guild):
        if not name:
            raise ValueError("name cannot be empty")
        self.name = name
        self.guild = guild

    # called as toString alternative for object
    def __str__(self):
        return f"{self.name}, is from {self.guild} magic guild"

    def cast(self):
        match self.guild:
            case "fire":
                return "luminar!!! ---> 🔥"
            case "water":
                return "bubble!! ---> 💧"
            case "land":
                return "fuji rise!!!! ----> 🗻"
            case "air":
                return "clenser!!  ---> 🌪️"
            case _:
                return "🚽"
    # getter
    @property
    def guild(self):
        return self._guild
    
    # setter
    @guild.setter
    def guild(self, guild):
        if guild not in ['air', 'water', 'fire', 'land']:
            raise ValueError("guild not in 4 elements")
        else:
            self._guild = guild
# @ are decorators and we use them wrt to getters and setters

# ... is a placeholder for later implementation
def main():
    wizard = get_wizard()
    # print(f"{wizard.name}:{wizard.guild}")
    print(wizard)
    # wizard.guild = "ice"
    print(wizard.cast())

def get_wizard():
#     name = input("Name: ")
#     guild = input("Guild: ")
#     return (name, guild) # returning a touple, its immutable
# # if we return a list return [name, guild] now we can change them later
    # student = {} # empty dict
    # student["name"] = input("Name: ")
    # student["guild"] = input("Guild: ")

    # wizard = Wizard() # created obj of wizard class
    # wizard.name = input("Name: ")
    # wizard.guild = input("Guild: ")
    # other way
    n1 = input("Name: ")
    g1 = input("Guild: ")
    return Wizard(n1, g1)

if __name__ == "__main__":
    main()