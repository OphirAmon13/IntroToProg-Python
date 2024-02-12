# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: Ophir Amon, 2/12/2024
# ------------------------------------------------------------------------------------------ #

# Import necessary functions
from sys import exit
import csv

# Define the Data Constants
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables and constants
student_first_name: str = ""  # Holds the first name of a student entered by the user.
student_last_name: str = ""  # Holds the last name of a student entered by the user.
course_name: str = ""  # Holds the name of a course entered by the user.
student_data: dict = {}  # One row of student data
students: list = []  # A table of student data
csv_data: str = "" # Stores data to be put into CSV file.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

def add_user(): # Adds user to database
    student_first_name = input("Enter the student's first name: ")
    if not student_first_name: # Checks if student_first_name is an empty string
        print("ERROR: Student first name cannot be empty!")
        return
    
    student_last_name = input("Enter the student's last name: ")
    if not student_last_name: # Checks if student_last_name is an empty string
        print("ERROR: Student last name cannot be empty!")
        return
    
    course_name = input("Please enter the name of the course: ")
    if not course_name: # Checks if course_name is an empty string
        print("ERROR: Course name cannot be empty!")
        return
    
    student_data = {   # Creates dictionary of the inputted student data
        "first_name": student_first_name,
        "last_name": student_last_name,
        "course_name": course_name
    }
    students.append(student_data) # Adds dictionary to list of all student data
    print(students)

def print_table(): # Presents all information to the user
    print("First Name \t\tLast Name \tCourse Name")
    for row in students:
        print(f"{row["first_name"]} \t\t{row["last_name"]} \t\t{row["course_name"]}")

def save_to_csv(): # Saves all information to CSV file
    with open(FILE_NAME, "w") as file:
        for row in students:
            csv_data = f"{row["first_name"]},{row["last_name"]},{row["course_name"]}\n"
            file.write(csv_data)
        for row in students:
            print(f"You have registered {row["first_name"]} {row["last_name"]} for {row["course_name"]}.")

def quit_program(): # Ends the program
    exit()


if __name__ == "__main__":
    students = []
    # Define the Data Constants
    MENU: str = '''
    ---- Course Registration Program ----
    Select from the following menu:  
        1. Register a Student for a Course.
        2. Show current data.  
        3. Save data to a file.
        4. Exit the program.
    ----------------------------------------- 
    '''
# Reads the contents of the file upon running program
try:
    with open(FILE_NAME, "r") as file:
        column_names = ("first_name", "last_name", "course_name")
        all_rows = csv.DictReader(file, fieldnames=column_names)
        for row in all_rows:
            students.append(row)
    print(students)
    print("INFO: All rows loaded from the database file!")
except FileNotFoundError as error_message:
    print("ERROR: Database file not found")
    print(f"Error detail: {error_message}")
except ValueError as error_message:
    print("ERROR: There was a value error exception when trying to open the file")
    print(f"Error detail: {error_message}")

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    user_choice = input("Please enter a menu option (1-4): ")
    match user_choice:
        case "1":
            add_user()
        case "2":
            print_table()     
        case "3":
            save_to_csv()
        case "4":
            quit_program()
        case _:
            print("ERROR: Please select a valid option")