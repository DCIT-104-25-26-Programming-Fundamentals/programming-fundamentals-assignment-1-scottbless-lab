# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def array_statistics_calculator():
    Numbers = []
    Total = 0
    count = int((input("How many numbers do you want to enter:")))
    for i in range(count) :
        num1 = int(input("Enter the number:"))
        
        if num1 <=0:
            print("ERROR")
        else:
         Numbers.append(num1)
    
    for i in Numbers:
            Total += i
    print("Sum:",Total)
    
    if len(Numbers) >  0  :  
        Average = Total / len(Numbers)
        print("Average:",Average)
    
        Maximum = Numbers[0]        
        for i in Numbers:
                if i > Maximum:
                    Maximum = i
        print("Maximum:",Maximum)
        Minimum = Numbers[0]            
    
        for i in Numbers:
                if i < Minimum:
                    Minimum = i
        print("Minimum:",Minimum)

array_statistics_calculator()
                        