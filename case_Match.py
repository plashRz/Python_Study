name = input("Enter your name: ").title().split(" ")

match name[len(name)-1]:
    case "Lanister":
        print("House of Lanister")
    case "Stark":
        print("House of Stark")
    case "Targaryen":
        print("House of Targaryen")
    case "Baratheon":
        print("House of Baratheon")    
    case "Snow" | "Sand" | "Pyke":
        print("Bastard")
    case _:
        print("Who are you?")                               