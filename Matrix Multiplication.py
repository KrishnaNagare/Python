'''1. Take input from user to perform matrix multiplication operation like addition and substraction. 
def get_matrix_input(rows, cols, matrix_name):'''
    """Function to get matrix input from the user."""
    print(f"Enter the elements of {matrix_name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        while len(row) != cols:
            print(f"Please enter exactly {cols} elements.")
            row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix.append(row)
    return matrix
def print_matrix(matrix):
    """Function to print a matrix."""
    for row in matrix:
        print(" ".join(map(str, row)))
def matrix_addition(matrix1, matrix2):
    """Function to perform matrix addition."""
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
def matrix_subtraction(matrix1, matrix2):
    """Function to perform matrix subtraction."""
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
def main():
    rows = int(input("Enter the number of rows for the matrices: "))
    cols = int(input("Enter the number of columns for the matrices: "))
    matrix1 = get_matrix_input(rows, cols, "Matrix 1")
    matrix2 = get_matrix_input(rows, cols, "Matrix 2")
    print("\nMatrix 1:")
    print_matrix(matrix1)
    print("\nMatrix 2:")
    print_matrix(matrix2)
    print("\nAddition of the matrices:")
    addition_result = matrix_addition(matrix1, matrix2)
    print_matrix(addition_result)
    print("\nSubtraction of the matrices (Matrix 1 - Matrix 2):")
    subtraction_result = matrix_subtraction(matrix1, matrix2)
    print_matrix(subtraction_result)

if __name__ == "__main__":
    main()
