"""Write a program that tells a user how many days there are in a specific month.
Use a dictionary to map the month numbers (1-12) to the number of days in
each month.
Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid
and print the number of days in the corresponding month.
"""
month_days = {
1:31,
2:28,
3:30,
4:31,
5:30,
6:31,
7:30,
8:31,
9:30,
10:31,
11:30,
12:31
}

# Define the dictionary with the numner of days in each month 
month_days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12 : 31
}

# Funtion to check f a year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Ask the user for the month number
month = int(input("please enter the month number (1-12): ")) 

#check if the month number is valid 
if 1 <=month <=12:
    #ask the user fo rthe year 
    year = int (input("please enter the year:"))
    
    #adjust for the febuary in leap year 
    if month == 2 and is_leap_year (year): #correct function call
        days = 29
    else:
        days = month_days[month]
        
        
        #output the number of the days 
        print(f"there are {days}days in month {month}of the year {year}")
        
else:
    print ("invalid month number. please enter a number between 1 and 12.")

        