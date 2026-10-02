print("************************************************************")
# 09_dictionaries.py
# Dictionaries - storing key-value pairs

# Creating dictionaries
person = {
    "name": "Darrrico",
    "age": 30,
    "city": "Los Angeles",
    "job": "AI Engineer"
}

# Accessing values by key
print("Name:", person["name"] + "Age:", person["age"])

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