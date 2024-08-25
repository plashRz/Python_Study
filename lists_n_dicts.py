# LIST example
creatures=["Gargoyles", "Windegoes", "Banshees", "Warewolves", "Sirens"]

for creature in creatures:
    print(creature)

# other way

for i in range(len(creatures)):
    print(i, "-->", creatures[i])

# DICT example
bio = {
        "Crow": "Air",
        "Tiger":"Land",
        "Shark":"Water",
        "Alligator":"Land/Water",
        "Sparrow":"Air",
       }

for life in bio:
    # print(life) # by default it fetches keys
    print(life, bio[life], sep="-->")


print("\n")
# Wombo-Combo 
guilds = [
    {"name":"Natsu", "guild":"Fairy Tail", "magic":"Fire DragonSlayer"},
    {"name":"Grey", "guild":"Fairy Tail", "magic":"Ice Maker"},
    {"name":"Ichiya", "guild":"Blue Pegasus", "magic":"Perfume"},
    {"name":"Jellal", "guild":None, "magic":"Heavenly Body"},
]

for member in guilds:
    print(member["name"], member["guild"], sep=" -> ")