"""Use your newly acquired knowledge of the for loop to complete the following
tasks. Print all values to the console in each case. * Write a loop that counts
up from 0 to 50 in increments of 1. * Write a loop that counts down from 50 to
0 in decrements of 1. * Write a loop that counts up from 30 to 50 in increments
of 1. * Write a loop that counts down from 50 to 10 in decrements of 2. * Write
a loop that counts up from 100 to 200 in increments of 5. You may include all
loops in a single project
"""
def fifty():
    for x in range (50):
     x = x + 1
    print(x)
    fifty()
    
def fifty():
 for y in range (51):
    y = 50 - y
    print(y)
fifty()
           
           
def thirty():
 for i in range (29,50):
    i = i + 1
    print(i)
thirty()
               
               
               
def two():
 for f in range (50,9,-2):
    print(f)
 two()
                       
                       
def hundo():
 for v in range (100,205,+5):
    print(v)
hundo()
                               
# Define a function named 'two'
def two():
    # Iterate through the range from 50 to 10 (exclusive) decrementing by 2
    for f in range(50, 9, -2):
        # Print each value in the range
        print(f)

# Call the 'two' function to execute its code
two()

# Define a function named 'hundo'
def hundo():
    # Iterate through the range from 100 to 205 (exclusive) incrementing by 5
    for v in range(100, 205, 5):
        # Print each value in the range
        print(v)

# Call the 'hundo' function to execute its code
hundo()

# Function to perform a counting loop with user-specified parameters
def count_loop(start, end, step, description):
    print(f"\n{description}")
    count = 0  # Track the number of iterations
    for i in range(start, end, step):
        print(i)
        count += 1
    print(f"Summary: {count} iterations from {start} to {end - step if step > 0 else end + step}.")

# Main function to define advanced requirements and run loops
def main():
    # Counting up from 0 to 50 in increments of 1
    count_loop(0, 51, 1, "Counting up from 0 to 50 in increments of 1:")

    # Counting down from 50 to 0 in decrements of 1
    count_loop(50, -1, -1, "Counting down from 50 to 0 in decrements of 1:")

    # Counting up from 30 to 50 in increments of 1
    count_loop(30, 51, 1, "Counting up from 30 to 50 in increments of 1:")

    # Counting down from 50 to 10 in decrements of 2
    count_loop(50, 9, -2, "Counting down from 50 to 10 in decrements of 2:")

    # Counting up from 100 to 200 in increments of 5
    count_loop(100, 201, 5, "Counting up from 100 to 200 in increments of 5:")

if __name__ == "__main__":
    main()
