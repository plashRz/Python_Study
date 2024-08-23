
# define a function if no value is provided default will be world 
def hello(to="World"):
    print ("Hello,", to)

# by putting main logic in a function we can get rid of the order of the functions dependency
def main():
    # demo for default value
    hello()
    # take input and pass in last name in the function
    name = input("Enter your name: ").strip().title().split(" ")
    hello(name[len(name)-1])

# Explicitly calling main function which sets the flow
main()
