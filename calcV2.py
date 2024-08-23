def main():
    num = int(input("Enter the number to be squared: "))
    print(f"Square of {num} is:", sq(num))

def sq(num):
    return pow(num,2) # or num*num || n ** 2

main() 