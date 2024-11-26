"""In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.
Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a
dictionary.
2. Print the values on separate lines using a single print() statement.
3. Use variables with appropriate data types for each piece of information.
"""

name = ("muhammad munim")
hometown = ("rawalpindi")
age = ("18")
print("name:" , name , "hometown:" , hometown , "age;", age )

def get_user_biography():
    
    # prompt the user for their full name (first and last)
    name == input("enter your full name (first and last): ")
    
    #prompt the user for their hometown
    hometown = input("enter your hometown: ")
    
    #loop to ensure valid input for age
    while True:
        age_input = input("enter your age: ") #ask for age input
        try:
            age = int(age_input) #attempt to convert the input to an integer 
            if age <0: #check if the age is negative 
             raise ValueError ("age cannot be negative.")
            break  # exit the loop i f age is valid
        except ValueError :
            #hande the case where input is invalid (not an integer or negative)
            print(f"invalid input for the age : '{age_input}'. please enter a positive integer.")
            
            #store the information in a dictionary
            biography ={
                "name" : name ,
                "hometown" : hometown ,
                "age" : age
            }
            
    return biography #return the biography dictioary
def print_biography(biography):

#print the values on separate line using a single print()statement
   print(f"name:{biography ['name']}inhometown:{biography['hometown']}inage:{biography}['age']")
def main():
    
    #get the users biography 
    biography = get_user_biography()
    
    #print the biography
    print_biography (biography)
    
    #entry point of the program 
    if __name__ == "__main__":
        main()
