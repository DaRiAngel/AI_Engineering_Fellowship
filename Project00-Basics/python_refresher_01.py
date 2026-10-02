####################################
name = "Alice"         # String (text)
age = 25               # Integer (whole number)
height = 5.6           # Float (decimal number)
is_student = True      # Boolean (True or False)
greeting = "Hello, " + name + "!"
print(greeting)
####################################

# Getting user input (input() always returns a string)
name = input("What's your name? ")
age_text = input("How old are you? ")
age = int(age_text)  # Convert string to integer
print("Nice to meet you, " + name + "!" + "You are", age, "years old")

# Shorter way to get and convert numbers
favorite_number_doubled = int(input("What's your favorite number? ")) * 2
print("Your favorite number doubled is:", favorite_number_doubled)

# Different ways to format output
print("Hello", name, "you are", age, "years old")
print(f"Hello {name}, you are {age} years old")  # f-string (modern way)

# Getting decimal numbers
temperature = float(input("What's the temperature today? "))
print(f"It's {temperature} degrees today")

####################################