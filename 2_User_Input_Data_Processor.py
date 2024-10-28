#Task 1: Input Length Validator

user_name = input("Please enter your full name (first and last names): ") # Ask the user for their first and last names

seperated_name = user_name.split() #seperat the names into first and last

if len(seperated_name[0]) >= 2 and len(seperated_name[1]) >= 2: #check that both names are atleast 2 characters long
    print("Your name is valid: meets the minimum requirements") #notify the user that both names meet the minimum requirements
else: #atleast one or both names shorter than 2 characters
    print("Your name is invalid: Both names should be atleast 2 characters long") #notify the user that names are not valid and give them valid criteria
