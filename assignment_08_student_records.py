# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
Student_Records_system = {}


def add_student():

    Name_of_student = input("Enter your name: ")
    User_ID = input("Enter your ID: ")

    Score = []

    Scores_to_enter = int(input("How many scores do you want to enter: "))

    for i in range(Scores_to_enter):
        Score_entry = int(input(f"Enter score {i+1}: "))
        Score.append(Score_entry)

    Average = sum(Score) / len(Score)

    Student_Records_system[User_ID] = {
        "Name": Name_of_student,
        "ID": User_ID,
        "Scores": Score,
        "Average": Average
    }

    print("Student record saved successfully.")


def display_all_student():

    if not Student_Records_system:
        print("No student records found.")
        return

    print("\n{:<18}{:<12}{:<25}{:<10}".format(
        "Name", "ID", "Scores", "Average"
    ))
    print("-" * 65)

    for student in Student_Records_system.values():

        scores = ", ".join(str(score) for score in student["Scores"])

        print("{:<18}{:<12}{:<25}{:<10.2f}".format(
            student["Name"],
            student["ID"],
            scores,
            student["Average"]
        ))


def average_score_calculation():

    User_ID = input("Enter student ID: ")

    if User_ID in Student_Records_system:

        individual_score = Student_Records_system[User_ID]["Scores"]

        average_score = sum(individual_score) / len(individual_score)

        scores = ", ".join(str(score) for score in individual_score)

        print("\nStudent Name:", Student_Records_system[User_ID]["Name"])
        print("Student ID:", User_ID)
        print("Scores:", scores)
        print(f"Average Score: {average_score:.2f}")

    else:
        print("Error: Student ID not found.")


while True:

    print("\n======= STUDENT RECORD SYSTEM MENU =======")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")

    Choose_from_the_menu = input("Choose from the menu: ")

    if Choose_from_the_menu == "1":

        add_student()

    elif Choose_from_the_menu == "2":

        display_all_student()

    elif Choose_from_the_menu == "3":

        average_score_calculation()

    elif Choose_from_the_menu == "4":

        print("Quitting.")
        break

    else:

        print("Invalid choice. Try again.")
