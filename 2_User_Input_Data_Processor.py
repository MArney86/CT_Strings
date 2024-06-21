def check_password(password): #function definition for Task 2
    has_upper = False #flag for having atleast one uppercase letter
    has_lower = False #flag for having atleast one lowercase letter
    has_number = False #flag for having atleast one number
    has_eight = False #flag to ensure that there are atleast 8 characters in the password

    if len(password) >= 8: #check that there are 8 characters in the password
        has_eight = True # set flag for character minimum to True
        for char in password: #iterate through the password characters
            if char.isupper(): # check current character if it's uppercase
                has_upper = True #set uppercase flag to True
            elif char.islower(): # chech current character if it's lowercase
                has_lower = True #set lowercase flag to True
            elif char.isdigit(): # check current character if it's a number
                has_number = True #set number flag to True

    if has_eight and has_number and has_lower and has_upper: #check if password flags are all true
        return "Your password is valid" #returnt that password is valid
    else: #not all flags are true
        return "Your password is invalid: The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number." #notify the user that password is invalid and give them proper criteria
   
#Task 1: Input Length Validator

user_name = input("Please enter your full name (first and last names): ") # Ask the user for their first and last names

seperated_name = user_name.split() #seperat the names into first and last

if len(seperated_name[0]) >= 2 and len(seperated_name[1]) >= 2: #check that both names are atleast 2 characters long
    print("Your name is valid: meets the minimum requirements") #notify the user that both names meet the minimum requirements
else: #atleast one or both names shorter than 2 characters
    print("Your name is invalid: Both names should be atleast 2 characters long") #notify the user that names are not valid and give them valid criteria

#Task 2: Password Complexity Checker

user_password = input("Please enter your password:") #ask for and store a password from the user
print(check_password(user_password)) #print the results from checking the password entered by the user with the check_password function

#Task 3: Email Formatter
#Implement a script that ensures all user email addresses are in a standard format
valid_domains = ["net", "com", "gov", "org", "edu", "cc", "int", "mil"]

user_email = input("please enter your email: ") #aske the user for an email address
if '@' in user_email: # verify that the
    split_email = user_email.split("@") #split the email at the @ symbol for easier testing
    if split_email[0] and len(split_email[0]) <= 64 and split_email[0].isalnum(): #check for valid identifier in the email address
        split_domain = split_email[1].split(".") #split the domain by the '.' symbol for validity
        if len(split_domain[0]) <= 63 and split_domain[0].isalnum(): #check for valid domain name
            if split_domain[1] in valid_domains: #check that the top level domain is valid
                print("This email is in a valid format") #let the user know the email address is valid
            else: #invalid top level domain
                print("Invalid email address: email adresses must have a top level domain of .net, .com, .gov, .org, .edu, .cc, .int, or .mil") #let the user know the list of acceptable top level domains for email addresses
        else: #invalid domain
            print("Invalid email address: email addresses must have a domain with a label of no more than 63 alphanumeric characters") #let the user know the minimum requirements for email domain
    else: #invalid identifier
        print("Invalid email address: email addresses must have a local space identifier that contains no more than 64 alphanumeric characters") #let the user know the minimum requirements for the identifier part of the email address
else: #no @ symbol
    print("Invalid email address: email addresses must contain the @ symbol") #let the user know that the email address must contain an @ symbol

