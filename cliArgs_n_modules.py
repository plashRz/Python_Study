import sys

# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("Please enter name as argument.")

# sys.exit(msg) just ends the program

if (len(sys.argv)<2):
    sys.exit("Enter atleast one argument")

# note 1: slices the arg array and starts from 1st argument arg instead of 0th argument
# to omit from end use neg number [1:-1]
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)

