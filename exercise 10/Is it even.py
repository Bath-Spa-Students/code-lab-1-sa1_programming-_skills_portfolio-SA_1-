"""Write a program that tests if a value is even or odd. Follow the instructions
outlined below:
Instructions:
• The program should ask the user for a number from within the main
function.
• The entered number should be passed to a function that determines if the
value is even or odd.
• The function should return a message indicating whether the number is
even or odd.
• The message returned by the function should be printed from within the
main function.
"""
def check_even_odd(n): return "even" if n % 2 == 0 else "odd"
n = int(input("Enter a number: "))
print(f"The number is {check_even_odd(n)}.")



# Prompt the user to enter a number and convert the input to an integer
n = int(input("Enter a number: "))

# Check if the number is even or odd using a conditional expression
# Print the result indicating whether the number is even or odd
print(f"The number is {'even' if n % 2 == 0 else 'odd'}.")


# Function to determine if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

# Main function to handle user input, display results, and provide a summary
def main():
    even_count = 0
    odd_count = 0
    
    while True:
        # Get user input with validation
        try:
            number = int(input("Enter a number to check if it's even or odd: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        # Check if the number is even or odd and display the result
        result = check_even_odd(number)
        print(result)

        # Update counters based on the result
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        # Ask if the user wants to check another number
        another = input("Do you want to check another number? (yes/no): ").strip().lower()
        if another != "yes":
            break

    # Display a summary of even and odd counts
    print("\nSummary:")
    print(f"Total even numbers: {even_count}")
    print(f"Total odd numbers: {odd_count}")
    print("Thank you for using the program!")

# Run the program
if __name__ == "__main__":
    main()
