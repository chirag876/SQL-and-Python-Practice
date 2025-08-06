"""
This script shows how to attach an attribute (like 'count') to a function in Python.
Useful when you want to track function behavior without using global variables or classes.
"""

# Define the function
def my_function():
    # Increase the count each time the function is called
    my_function.count += 1

    # Print a message showing how many times the function has been called
    print(f"my_function has been called {my_function.count} times.")

# Attach a custom attribute to the function
my_function.count = 0  # Initializing count

# Call the function multiple times
my_function()
my_function()
my_function()

# You can also access the attribute outside the function
print(f"\nFinal count: {my_function.count}")

# Output:
# my_function has been called 1 times.
# my_function has been called 2 times.
# my_function has been called 3 times.

# Final count: 3
