# Take a input prompt and assign that value to a variable {combined string functions}
name=input("Whats your name? ").strip().title()

# String functons few  examples
# name = name.strip().title()
# we can chain these functions
# split users name
fname, lname = name.split(" ")

# Print value of that variable and say hello to it.
# print("hello, "+name) or below
# print("hello, ", name, end="", sep="===")
# print(name)
# new way

print(f"Hello, {fname}")
print("Welcome Back!")

