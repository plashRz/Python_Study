
# define a function if no value is provided default will be world 
def hello(to="World"):
    return f"Hello, {to}"

# by putting main logic in a function we can get rid of the order of the functions dependency
def main():
    # demo for default value
    print(hello())
    # take input and pass in last name in the function
    name = input("Enter your name: ").strip().title().split(" ")
    print(hello(name[len(name)-1]))

# Explicitly calling main function which sets the flow
if __name__ == "__main__":
    main()
