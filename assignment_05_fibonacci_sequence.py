# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_fibonacci(n):

    if n <= 0:
        print("Error! Your number is be a negative integer.Enter a positive integer")
        return

    number_before = 0
    number_after = 1

    print("Fibonacci sequence:", end=" ")

    for i in range(n):
        print(number_before, end=" ")

        next_number = number_before + number_after
        number_before = number_after
        number_after = next_number

    print()


def check_fibonacci(number):

    if number < 0:
        print(number, "is not a Fibonacci number.")
        return

    number_before = 0
    nummber_after = 1

    while number_before < number:
        next_number = number_before + nummber_after
        number_before = nummber_after
        nummber_after = next_number

    if number_before == number:
        print(number, "is a Fibonacci number.")
    else:
        print(number, "is NOT a Fibonacci number.")


n = int(input("How many terms? "))
print_fibonacci(n)

number = int(input("Enter a number to check: "))
check_fibonacci(number)