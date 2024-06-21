#Task 1:
commands = ["help", "issue", "contact support", "service", "account"] #list of recognized commands
responses  = [
    "I'm here to help!", "What sort of issue are you having? ", 
    "I'd be happy to help you with support, you can also call us at 1-800-555-5555 for a live person.", 
    "I can help you review or change the services on your account.", 
    "Let's get you verified so I can pull up your account information."] # Responses for the commands list
issues = ['login', 'performance', 'error', 'billing', 'features', 'discounts'] #issue categories for Task 2

user_command = input("Hello there!!! \n What can I help you with today?: ") #welcome the user and ask them for a command
split_user_command = user_command.split() #split the response into individual words to search more easily for commands
command_exists = False #flag in case there is not a command in the user's response
for word in split_user_command: #iterate the words from the user's response
    if word.lower() in commands: #check if the current word from the iteration is in the commands list
        ###TASK 2###
        if word.lower() == commands[1]: # test if the command statement contains issue for Task 2
            command_exists = True #set command flag to True
            issue_exists = False #Flag in case user input doesn't contain a known issue category
            user_issue = input(responses[1]) #get the issue category of the user's issue
            user_response = user_issue.split() #split the user's response to make it easier to iterate
            for response in user_response: #iterate the user response
                if response.lower() in issues: #check if the current word is in the list of issue categories
                    print(f"Attention Support Team:\nIssue Category: {response}") #response once issue category found
                    issue_exists = True # Set the flag that a categorizable issue was found
                else: #word not in issue categories
                    continue #move on to next iteration
            if not issue_exists: #check if an issue category was found
                print("I'm sorry, I didn't understand what issue you were describing") #message to let the user know that there was not issue category in their response
        ### END TASK 2###
        print(responses[commands.index(word)]) #print the response for the command in the user's response
        command_exists = True #set command flag to True
    else: #no command in this iteration
        continue #continue iteration
if not command_exists: #check if no command was in the response
    print("Hmmm... I'm sorry, I didn't understand what you said.") #Let the user know that no known command was present in their response
