print("************************************************************")
# 08_functions.py
# Functions - reusable blocks of code

# Basic function definitions
# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")
    print(f"Nice to meet you, {name}!")
greet_person("Bob")

# Function with multiple parameters
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)
add_numbers(10, 20)

# Function that returns a value
def multiply(x, y):
    return x * y

result = multiply(4, 7)
print("4 × 7 =", result)

# Function with default parameters
def introduce(name, age=25):
    print(f"Hi, I'm {name} and I'm {age} years old")

introduce("Charlie")      # Uses default age of 25
introduce("Diana", 30)    # Uses provided age of 30

# Function that works with lists
def find_max(numbers):
    if not numbers:  # Check if list is empty
        return None

    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

my_numbers = [3, 7, 2, 9, 1, 8]
biggest = find_max(my_numbers)
print("Biggest number:", biggest)

# Function with multiple return values
def get_name_parts(full_name):
    parts = full_name.split()
    first_name = parts[0]
    last_name = parts[-1]
    return first_name, last_name

first, last = get_name_parts("John Smith")
print("First name:", first)
print("Last name:", last)

# Using functions to organize code
def main():
    print("Welcome to the calculator!")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    sum_result = add_numbers_return(num1, num2)
    product_result = multiply(num1, num2)

    print(f"Sum: {sum_result}")
    print(f"Product: {product_result}")

def add_numbers_return(a, b):
    return a + b



# Run the main function
if __name__ == "__main__":
    main()


print("************************************************************")
# 09_dictionaries.py
# Dictionaries - storing key-value pairs

# Creating dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "job": "Engineer"
}

# Accessing values by key
print("Name:", person["name"])
print("Age:", person["age"])

# Safer way to access (won't crash if key doesn't exist)
print("Name:", person.get("name"))
print("Country:", person.get("country", "Unknown"))  # Default value

# Adding new key-value pairs
person["email"] = "alice@email.com"
person["hobby"] = "reading"

print("Updated person:", person)

# Modifying existing values
person["age"] = 31
print("New age:", person["age"])

# Checking if key exists
if "name" in person:
    print("Person has a name!")

# Getting all keys, values, or items
print("\nAll keys:", list(person.keys()))
print("All values:", list(person.values()))
print("All items:", list(person.items()))

# Looping through dictionaries
print("\nPerson details:")
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary of lists
grades = {
    "math": [85, 90, 88],
    "english": [92, 87, 95],
    "science": [78, 82, 85]
}

print("\nGrades:")
for subject, scores in grades.items():
    average = sum(scores) / len(scores)
    print(f"{subject}: {scores} (Average: {average:.1f})")

# List of dictionaries
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

print("\nStudent grades:")
for student in students:
    print(f"{student['name']}: {student['grade']}")

# Nested dictionaries
school = {
    "name": "Central High",
    "classes": {
        "math": {"teacher": "Mr. Smith", "students": 25},
        "english": {"teacher": "Ms. Johnson", "students": 22}
    }
}

print("\nMath teacher:", school["classes"]["math"]["teacher"])
print("************************************************************")
# 10_file_handling.py
# Reading from and writing to files

# Writing to a file
def write_to_file():
    # Create and write to a file
    with open("sample.txt", "w") as file:
        file.write("Hello, this is my first file!\n")
        file.write("Python makes file handling easy.\n")
        file.write("This is the third line.\n")

    print("File 'sample.txt' has been created!")

# Reading from a file
def read_entire_file():
    try:
        with open("sample.txt", "r") as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print("File not found! Make sure to run write_to_file() first.")

# Reading line by line
def read_line_by_line():
    try:
        with open("sample.txt", "r") as file:
            print("Reading line by line:")
            line_number = 1
            for line in file:
                print(f"Line {line_number}: {line.strip()}")
                line_number += 1
    except FileNotFoundError:
        print("File not found!")

# Appending to a file
def append_to_file():
    with open("sample.txt", "a") as file:
        file.write("This line was added later.\n")
        file.write("You can append multiple lines!\n")

    print("Text appended to file!")

# Working with CSV-like data
def write_student_data():
    students = [
        "Alice,85,Math",
        "Bob,92,Science",
        "Charlie,78,English"
    ]

    with open("students.txt", "w") as file:
        file.write("Name,Grade,Subject\n")  # Header
        for student in students:
            file.write(student + "\n")

    print("Student data written to 'students.txt'!")

def read_student_data():
    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()
            print("Student data:")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("Student file not found!")

# Example of processing file data
def analyze_student_data():
    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

            # Skip header line
            for line in lines[1:]:
                parts = line.strip().split(",")
                name = parts[0]
                grade = int(parts[1])
                subject = parts[2]

                if grade >= 90:
                    print(f"{name} got an A in {subject}!")
                elif grade >= 80:
                    print(f"{name} got a B in {subject}")
                else:
                    print(f"{name} needs improvement in {subject}")

    except FileNotFoundError:
        print("Student file not found!")
    except (ValueError, IndexError):
        print("Error reading file data!")

# Main function to demonstrate all file operations
def main():
    print("File Handling Demo")
    print("=" * 20)

    # Create a file
    write_to_file()

    # Read the file
    read_entire_file()

    # Read line by line
    read_line_by_line()

    # Append to file
    append_to_file()
    read_entire_file()

    # Work with structured data
    write_student_data()
    read_student_data()
    analyze_student_data()

if __name__ == "__main__":
    main()