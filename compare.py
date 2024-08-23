def main():
    x = int(input("Enter 1st number "))
    y = int(input("Enter 2nd number "))
    score = int(input("Enter your score "))
    
    compare(x, y)

    print(grading(score))

    if oddEven(score):
        print(f"{score}: is Even")
    else:
        print(f"{score}: is Odd")    

# A function to grade scores
def grading(scores):
    if 90 <= scores <=100:
        return "Grade: A"
    elif scores >= 80 and scores < 90:
        return "Grade: B"
    elif scores >= 70 and scores < 80:
        return "Grade: C"
    elif scores >= 60 and scores < 70:
        return "Grade: D"
    elif scores < 60:
        return "Grade: F"
    else:
        return "Grade: Not Defined"

# A function to determine if a number is odd or even  
def oddEven(scores):
    # return True if scores % 2 == 0 else False
    #   or
    # if scores % 2 == 0:
    #     return True
    # else:
    #     return False
    #   or
    return (scores % 2 == 0)    

# A function to compare 2 numbers
def compare(x,y):
    if x<y:
        print(f"X:{x} is less than Y:{y}")
    elif x>y:
        print(f"X:{x} is greater than Y:{y}")
    else:
        print(f"X:{x} is equal to Y:{y}")

main()