x = int(input("Enter 1st number "))
y = int(input("Enter 2nd number "))
score = int(input("Enter your score "))

if x<y:
    print(f"X:{x} is less than Y:{y}")
elif x>y:
    print(f"X:{x} is greater than Y:{y}")
else:
    print(f"X:{x} is equal to Y:{y}")

def grading(scores):
    if 90 <= scores <=100:
        return "Grade: A"
    elif scores >= 80 and scores < 90:
        return "Grade: B"
    elif scores >= 70 and scores < 80:
        return "Grade: C"
    elif scores >= 60 and scores < 70:
        return "Grade: D"
    else:
        return "Grade: F"

print(grading(score))