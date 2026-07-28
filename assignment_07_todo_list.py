# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


List_of_task = []

def add_the_task():
    Number_of_task = int(input("Enter the number of tasks: "))

    for i in range(Number_of_task):
        task = input("Enter your task description: ")
        List_of_task.append(task)
        print("Task added:", task)


def view_the_task():
    if len(List_of_task) == 0:
        print("No Task available")
    else:
        print("Your Tasks:")
        a = 0
        for i in List_of_task:
            a += 1
            print(a, ".", i)


def delete_the_task():
    if len(List_of_task) == 0:
        print("No Task available")
    else:
        print("Your Tasks:")
        a = 0
        for i in List_of_task:
            a += 1
            print(a, ".", i)

        Task_to_remove = int(input("Enter the task you want to delete: "))

        if 1 <= Task_to_remove <= len(List_of_task):
            Remove_task = List_of_task.pop(Task_to_remove - 1)
            print(Remove_task, "has been deleted successfully.")

            print("Updated Task List:")
            if len(List_of_task) == 0:
                print("No Task available")
            else:
                a = 0
                for i in List_of_task:
                    a += 1
                    print(a, ".", i)
        else:
            print("Invalid task number, try again.")


while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    Choose_from_the_menu = input("Enter a number: ")

    if Choose_from_the_menu == "1":
        add_the_task()

    elif Choose_from_the_menu == "2":
        view_the_task()

    elif Choose_from_the_menu == "3":
        delete_the_task()

    elif Choose_from_the_menu == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select a number between 1 and 4.")