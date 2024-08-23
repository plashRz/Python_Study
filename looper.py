# Basic while loop example
def whiler(counter):
    while counter != 0:
        print(f"While Loop Counter at:{counter}")
        counter-=1 


# For looping certain times we use range eg: for i in range(100)
# If i never used we can use a place holder _ eg: for _ in range(100)
# Cheeky way: print("hello\n"*3, end="")
def forLooper(ToDo):
    for i in ToDo:
        print(f"ToDo Item: {i}")


# Break and Continue example
# we can flip conditions if n > 0: we can break, no need for continue part.
def BnC():
    while True:
        n = int(input("Input a positive number: "))
        if n < 0:
            continue
        else:
            print(f"Thanks for choosing: {n}")
            break
    return n


def main():
    ToDo=["Eat","Sleep","Study","Buy Stuff","Work a lil"]
    whiler(BnC()) # Returned a positive value from BnC and fed it to Whiler
    forLooper(ToDo)


main()