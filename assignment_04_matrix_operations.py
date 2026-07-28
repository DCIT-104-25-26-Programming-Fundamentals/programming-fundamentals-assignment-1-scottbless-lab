# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))

        while len(row) != cols:
            print(f"Please enter exactly {cols} numbers.")
            row = list(map(int, input(f"Enter row {i+1}: ").split()))

        matrix.append(row)

    return matrix

def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end="\t")
        print()
        
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(matrix[j][i])
        transpose.append(new_row)

    return transpose


def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] + B[i][j])
        result.append(row)

    return result


def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = []

    for i in range(rows_A):
        row = []

        for j in range(cols_B):
            total = 0

            for k in range(cols_A):
                total += A[i][k] * B[k][j]

            row.append(total)

        result.append(row)

    return result


print("PART A - TRANSPOSE MATRIX")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = read_matrix(rows, cols)

print("\nOriginal Matrix:")
display_matrix(matrix)

transpose = transpose_matrix(matrix)

print("\nTranspose Matrix:")
display_matrix(transpose)


print("\nPART B - ADD TWO MATRICES")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter Matrix A")
A = read_matrix(rows, cols)

print("Enter Matrix B")
B = read_matrix(rows, cols)

sum_matrix = add_matrices(A, B)

print("\nResult of Addition:")
display_matrix(sum_matrix)


print("\nPART C - MULTIPLY TWO MATRICES")

print("Enter Matrix A")
rows_A = int(input("Rows: "))
cols_A = int(input("Columns: "))

A = read_matrix(rows_A, cols_A)

print("Enter Matrix B")
rows_B = int(input("Rows: "))
cols_B = int(input("Columns: "))

if cols_A != rows_B:
    print("Matrix multiplication is not possible.")
else:
    B = read_matrix(rows_B, cols_B)

    product = multiply_matrices(A, B)

    print("\nResult of Multiplication:")
    display_matrix(product)