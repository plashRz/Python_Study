import csv

def filler():
    name =  input("Enter the name: ").strip().title()
    role = input("Role: ").strip().title()
    return f"{name},{role}\n"

with open("aka.csv", 'a') as file:
    file.write(filler())
    # other way 
    # writer = csv.writer(file)
    # writer.writerow([name, role])

    # write = csv.dictwriter(file, fieldnames=['name', 'role'])
    # writer.writerow({"name": name,  "role": role})

with open("aka.csv") as file:
    # for line in sorted(file):
    #     row = line.rstrip().split(",") # we can also do row, col have separate variable for each element
    #     print(f"{row[0]} is a: {row[1]}")
    reader = csv.reader(file)
    for row, col in reader:
        print(f"{row} is a: {col}")

# csv.DictReader reads as a dict instead of list 
# have to add hints in csv file ie add row at top with name
# lambda is a no name function
# eg key= lambda student: student["name"]