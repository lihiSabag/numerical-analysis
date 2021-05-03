#  Creating a matrix of coefficients and the result vector
def create_square_matrix(size):

    mat = [0] * size
    b = list(range(size))
    for row in range(size):
        mat[row] = [0] * size
        for col in range(size):
            mat[row][col] = float(input(f"Matrix[{row}],[{col}]: "))
        b[row] = float(input(f"b[{row}] = "))
    return mat, b


# Checks if the matrix has a dominant diagonal then returns true, else returns false
def check_dominant_diagonal(mat):

    size = len(mat)
    if not mat:
        print("The matrix is not initialized ")
        return
    for i in range(size):
        pivot = mat[i][i]
        rowSum = 0
        for j in range(size):
            if i != j:
                rowSum += abs(mat[i][j])
        if abs(pivot) <= rowSum:
            return False
    return True


#  Jacobi iterative method
def jacobi_method(mat, result, lastRow):

    size = len(mat)
    var = []
    for col in range(0, size):
        res = result[col]
        for row in range(0, size):
            if col != row:
                res -= mat[col][row] * lastRow[row]
        var.append(res / mat[col][col])
    return var


#  Gaussian-seidel iterative method
def gaussian_seidel_method(mat, result, lastRow):

    size = len(mat)
    var = list(lastRow)
    for col in range(size):
        res = result[col]
        for row in range(0, size):
            if col != row:
                res -= mat[col][row] * var[row]
        var[col] = res / mat[col][col]
    return var


# Returns the row index with the maximum value
def max_val_index(mat, col):

    maxVal = abs(mat[col][col])
    index = col
    for row in range(col+1, len(mat)):
        if abs(mat[row][col]) > maxVal:
            maxVal = abs(mat[row][col])
            index = row
    return index


# swap between rows in the matrix
def swapRows(mat, r1, r2):
    tmp = mat[r1]
    mat[r1] = mat[r2]
    mat[r2] = tmp
    return mat


def pivoting(mat):
    size = len(mat)
    for col in range(size):
        maxValIndex = max_val_index(mat, col)  # the row index with the maximum value
        if maxValIndex != col:
            mat = swapRows(mat, col, maxValIndex)
    return mat


#  check if the absolute value for each variable in solution subtracted from the next solution
#  is lower than the  epsilon
def check_condition(epsilon, xr, xr_1):

    for x in range(0, len(xr)):
        if abs(xr_1[x] - xr[x]) < epsilon:
            return False
    return True


def iterative_method(iterative_method_name, mat, result, xr, epsilon):

    count = 0  # Iteration count
    condition = True
    if check_dominant_diagonal(mat):
        print("The matrix has a dominant diagonal")
        while condition:
            xr_1 = iterative_method_name(mat, result, xr)
            output = list(map(lambda y: "{:.4f}".format(y), xr_1))
            print(f"{count + 1}\t{output}")
            condition = check_condition(epsilon, xr, xr_1)
            xr = xr_1.copy()
            count += 1
        output = list(map(lambda y: "{:.4f}".format(y), xr))
        print(f"Final result:{output}")

    else:
        print("The matrix has no dominant diagonal")


def main():

    print("How would you like to run the exercise:")
    print("1. Create matrix")
    print("2. Using an existing example (default)")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        size = int(input("Enter size for the matrix (square matrix): "))
        mat, result = create_square_matrix(size)
    else:
        mat = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
        result = [2, 6, 5]

    epsilon = 0.00001
    xr = [0] * len(mat)  # Create a list of zeros
    mat = pivoting(mat)
    print("Choose an iterative method:")
    print("1. Jacobi method")
    print("2. Gaussian Seidel method (default)")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        iterative_method(jacobi_method, mat, result, xr, epsilon)
    else:
        iterative_method(gaussian_seidel_method, mat, result, xr, epsilon)


main()
