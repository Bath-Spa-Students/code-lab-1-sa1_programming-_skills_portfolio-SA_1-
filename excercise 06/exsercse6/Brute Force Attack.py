"""Write a program that simulates a password entry system. The correct password
is defined as 12345. The program should keep asking the user to enter the

password until they provide the correct one.
"""
Password = "12345"

while True:
    EnterPassword = input("Enter the password")
    if EnterPassword == Password:
        print("Correct Password Access Granted!")
        break
    else:
        print("Worng Password Access Denied!")
        
# Define the correct password
# Start an endless loop to get the password from the user
# Ask the user to type the password
# Verifying if the entered password matches the correct password
# If the password is incorrect make them step out and continue the loop


def password_entry_system():
    #define the correct password 
    correct_password = 12345
    #set maximum  number of attempts 
    maxx_attempts = 5
    #initialize the atempt counter
    attempts = 0 
    
    
    #use a while loop to repeadtely ask for the password 
    while attempts < max_attempts: # type: ignore
        #prompt the user for the password 
        user_input = input("enter password: ")
        
        #chek if the entred password is correct 
        if user_input : correct_password 
        print ("access granted. welcome!")
        break #exit the loop if the password is correct 
    else:
        attempts += 1 # increment the attempts counter 
        remaining_attempts = max_attempts - attempts # type: ignore
        if remaing_attempts > 0: # type: ignore
            print(f"incorrect password. you have reached the macimum number of attempts.")
        else: 
            print("incorrect password. you have reached the maximum number of attempts.")
            print("authorities have been alerted.")
            
            #call the function to ececute the program
            password_entry_system()