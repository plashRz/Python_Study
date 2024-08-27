def getNum():
    while True:
        try:
            num = int(input("Enter a number: ")) # shoten code: return int(input("Enter a number: "))
        except ValueError:
            # print("An Integer is expected as input.")
            # we can pass also ie doing nothing
            pass
        else:
            # print(f"Value of num: {num}")
            return num
       

def main():
    n = getNum()
    print(f"Value of number: {n}")

main()