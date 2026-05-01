
#Program 1: Exceptions

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ValueError:
    print("Error: Invalid input. Please enter integers only.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Operation complete.")

print() #spacing between programs

#Program 2: Modules

import math
import random

def generate_random_and_calculate():
    number = random.randint(1, 100)
    square_root = math.sqrt(number)

    print(f"Random number: {number}")
    print(f"Square root: {square_root}")

    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
    print()

for i in range(5):
    generate_random_and_calculate()

print() #spacing between programs

#Program 3: File Operations

import datetime

filename = "sample.txt"

# Step 1: Tries to read file name, creates if missing
try:
    with open(filename, "r") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"The file '{filename}' does not exist. Creating it now...")
    with open(filename, "w") as f:
        f.write("This is a sample file for Assignment 4.")

# Step 2: Prints current contents
with open(filename, "r") as f:
    contents = f.read()
print(f"Contents of '{filename}':")
print(contents)

# Step 3: Appends current datetime
now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
with open(filename, "a") as f:
    f.write(f"\nAppended on: {timestamp}")

# Step 4: Prints updated contents
with open(filename, "r") as f:
    updated = f.read()
print(f"\nUpdated contents of '{filename}':")
print(updated)
