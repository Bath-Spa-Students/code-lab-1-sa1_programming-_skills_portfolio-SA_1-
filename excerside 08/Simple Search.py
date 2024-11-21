"""Write a program that searches for a specific string within a list of strings. The list
is initialized with specific names (“Jake” “Zac”, “Ian”, “Ron”, “Sam”, “Dave”).
, and your task is to search for “Sam”.
"""

names = ["jake","zac","lan","ron","sam","dave"]
name_needed = "sam"

if name_needed in names:
    print (f"{name_needed} has been found in the list")
else:
    print (f"{name_needed} has not fount in the list1")
    
    
# Specify the name we are looking for
# Check if the specified name is in the list of names
# If the name is found, print a confirmation message
# If the name is not found, print a message indicating it wasn't found


#initialize the list with some names
names_list = ["jake"] , ["zac"] , ["ian"] , ["ron"] , ["sam"] , ["dave"]

#function to add names to the list 
def add_names():
    print("would you like to add more names to the list? (type 'yes' or 'no')")
    while input() . strip() . lower() == "yes":
        new_name = input("enter a name to add:"). strip()
        if new_name:
            names_list.append ()
            print(f"{new_name}has been added.")
        else:
            print ("invalid input> please enter a valid name.")
            print("add another?(type'yes' or 'no')")\
                
                
#function to search for a name with advanced requirements
def search_names (search_term):
    #case-insensitive and partial matvh search
    search_term = search_term.lower()
    matches = [name for name in names_list if search_term in name.lower()]
    
    #display the results
    if matches:
        print(f"\nfound {len(matches)} match (es) for ' {search_term}' : {' , '.join(matches)}")
    else:
        print("\no match found for ' {search_term}' .")
        
#main function to run the advance search 
def main():
    print ("initiall list of names:" , names_list)
    add_names() #allow usesr to add more names to the list 
    
    #allow the user to input the search term
    search_term = input ("enter the naem you want to search for "). strip()
    search_name (munim) # type: ignore
    
if __name__ == "__main__":
    main()
