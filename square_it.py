def main():
    num = int(input("Enter the number to be squared: "))
    print(f"Square of {num} is:", sq(num))

def sq(num):
    return pow(num,2) # or num*num || n ** 2

# __name__ is the name of the caller typically main when ran from terminal.
if __name__ == "__main__":
    main() 