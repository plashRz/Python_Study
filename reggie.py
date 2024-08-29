import re

email =  input("Enter your email address ").strip()

# # without regex
# flag = True
# try:
#     user, domain = email.split("@")
#     flag = False
# except ValueError:
#     pass

# try:
#     if user and "." in domain:
#         print(f"User: {user} & domain: {domain} -- Valid email address.")
#         flag = False
#     else:
#         flag = True     
# except NameError:
#     pass

# if flag is True:
#     print("Invalid email address")    


# . any character except newline
# * 0  or more characters
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m-n} repetitions
# ^ start of the string
# $ end of the string
# [] set of  characters
# [^] negate set of characters

# flags: re.ignorecase re.multiline re.dotall
if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|net|org|in)$", email, re.IGNORECASE):                   
    # .+ ..* gets the same result.  
    # r indicates raw string
    # [^@] anything but @
    # \w -> [a-zA-Z0-9_] word character
    # \d decimal digit
    # \D non decimal digit
    # \s whitespace characters
    # \S not a whitespace character
    # \W not a word character

    # A|B a or b
    # (...) a group
    # (?:....) non capturing groups

    print("Valid email address")
else:
    print("Invalid email address")    

    
# re.match returns groups of matches
# re.search
# re.sub  find and replace using regex