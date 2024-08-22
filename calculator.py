# int datatype
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# Float datatype
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = round(num1+num2)
# division = round(num1/num2,2)
division = round(num1/num2)

print(f"{addition:,}",'||',num1+num2) # formated with a ,
print(f"{division:.2f}",'||',num1/num2)

