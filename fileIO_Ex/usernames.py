# w for write/rewrite, a for append
# file = open("users.txt", 'a')
#   file.close()
# file.close() not needed when implementing via with syntax
with open("users.txt", 'a') as file:
    file.write(f"{input("Enter the Username:").strip().title()}\n")

# Reading
with open("users.txt", 'r') as file:
    # lines = file.readlines()
    for line in sorted(file, reverse=True):
        print(f"Hello, {line.rstrip()}") # end="" also a solution
