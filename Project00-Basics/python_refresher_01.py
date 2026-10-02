####################################
print("*"*60)
name = "You"         # String (text)
age = 25               # Integer (whole number)
height = 5.6           # Float (decimal number)
is_student = True      # Boolean (True or False)
greeting = "Hello, " + name + "!"
print(greeting)
####################################
print("*"*60)
# Getting user input (input() always returns a string)
name = input("What's your name? ")
age_text = input("How old are you? ")
age = int(age_text)  # Convert string to integer
print("Nice to meet you, " + name + "!" + "\nYou are", age, "years old")

print("*"*60)
# Shorter way to get and convert numbers
favorite_number_doubled = int(input("What's your favorite number? ")) * 2
print("Your favorite number doubled is:", favorite_number_doubled)

# Different ways to format output
print("Using nofstring \t", name, ":", age)
print(f"Using fstring \t\t{name}:{age}")  # f-string (modern way)

# Getting decimal numbers
temperature = float(input("What's the temperature today? "))
print(f"It's {temperature} degrees today")

####################################
print("*"*60)
# 04_basic_math.py
# Basic mathematical operations in Python

# Basic arithmetic operators
a,b = 10,3
print("Addition:", a + b)       # 13
print("Subtraction:", a - b)    # 7
print("Multiplication:", a * b) # 30
print("Division:", a / b)       # 3.333...
print("Integer division:", a // b) # 3 (rounds down)
print("Remainder:", a % b)      # 1 (modulo)
print("Power:", a ** b)         # 1000 (10 to the power of 3)
print("2 + 3 * 4 =", 2 + 3 * 4)  # 14 (not 20!) # Order of operations (PEMDAS) 
print("(2 + 3) * 4 =", (2 + 3) * 4)  # 20 # Use parentheses to change order

print("*"*60)
# Useful built-in functions
print("Absolute value of -5:", abs(-5))
print("Round 3.7:", round(3.7))
print("Maximum of 5, 8, 3:", max(5, 8, 3))
print("Minimum of 5, 8, 3:", min(5, 8, 3))

print("*"*60)
# Compound assignment operators
x = 5
x += 3  # Same as x = x + 3
x *= 2  # Same as x = x * 2
print("x after += 3:", x)
print("x after *= 2:", x)
print("*"*60)
print("*"*60)