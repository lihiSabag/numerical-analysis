
# create Identity matrix
def identity_matrix(size):
    I = list(range(size))
    for i in range(size):
        I[i] = list(range(size))
        for j in range(size):
            if i == j:
                I[i][j] = 1
            else:
                I[i][j] = 0
    return I


def machine_epsilon():
    eps = 1
    while (1 + eps) > 1:
        eps = eps / 2

    eps = eps * 2
    return eps


# Returns the row index with the maximum value
def max_val_index(mat, col):
    max = abs(mat[col][col])
    index = col
    for row in range(col, len(mat)):
        if abs(mat[row][col]) > max:
            max = abs(mat[row][col])
            index = row
    return index


# Returns Matrix - The result of multiplying two matrices
def mul_matrix(m1, m2):
    len_m1 = len(m1)
    cols_m1 = len(m1[0])
    rows_m2 = len(m2)
    if cols_m1 != rows_m2:  # Checks if it is valid to multiply between matrix
        print("Cannot multiply between matrix (incorrect size)")
        return
    new_mat = list(range(len_m1))
    val = 0
    for i in range(len_m1):
        new_mat[i] = list(range(rows_m2))
        for j in range(len(m2[0])):
            for k in range(cols_m1):
                val += m1[i][k] * m2[k][j]
            new_mat[i][j] = val
            val = 0
    return new_mat


# Returns the result matrix of  matrix *  vector
def mul_matrix_wVector(m, v):
    len_m = len(m)
    cols_m = len(m[0])
    rows_v = len(v)
    if cols_m != rows_v:  # Checks if it is valid to multiply between matrix
        print("Cannot multiply between matrix (incorrect size)")
        return
    new_mat = list(range(len_m))
    val = 0
    for i in range(len_m):
        for k in range(len(m[0])):
            val += m[i][k] * v[k]
        new_mat[i] = val
        val = 0
    return new_mat


# returns thr inverse matrix
def inverse(mat):
    size = len(mat)
    invert_mat = identity_matrix(size)
    for col in range(size):
        elem_mat = identity_matrix(size)
        # pivoting
        #if mat[col][col] == 0:
        max_row = max_val_index(mat, col)  # Returns the index of the row with the maximum value in the column
        invert_mat = mul_matrix(eMatForSwap(size, col, max_row), invert_mat)  # Elementary matrix for swap rows
        mat = mul_matrix(eMatForSwap(size, col, max_row), mat)  # swap between rows in case the pivot is 0
        pivot = mat[col][col]
        for row in range(size):
            if row != col and mat[row][col] != 0:
                elem_mat[row][col] = (-1) * (mat[row][col] / pivot)
        mat = mul_matrix(elem_mat, mat)
        invert_mat = mul_matrix(elem_mat, invert_mat)
    # check diagonal numbers
    for i in range(size):
        pivot = mat[i][i]
        if pivot != 1:
            for col in range(size):
                invert_mat[i][col] /= float(pivot)
            mat[i][i] = 1
    return invert_mat


# return element matrix for swap between row index1 to row in index2
def eMatForSwap(size, index1, index2):
    mat = identity_matrix(size)
    # swap rows
    tmp = mat[index1]
    mat[index1] = mat[index2]
    mat[index2] = tmp
    return mat


#  Calculates the "L" matrix and the "U" matrix
def LU(mat):
    size = len(mat)
    invert_mat = identity_matrix(len(mat))
    L = identity_matrix(size)
    for col in range(size):
        elem_mat = identity_matrix(size)
        if mat[col][col] == 0:  # Checks if there is zero on the diagonal
            max_row = max_val_index(mat, col)  # Returns the index of the row with the maximum value in the column
            invert_mat = mul_matrix(eMatForSwap(size, col, max_row), invert_mat)  # Elementary matrix for swap rows
            mat = mul_matrix(eMatForSwap(size, col, max_row), mat)  # swap between rows in case the pivot is
        pivot = mat[col][col]
        for row in range(col+1, size):
            if mat[row][col] != 0:
                elem_mat[row][col] = mat[row][col] / pivot * -1  # Calculate the appropriate elementary matrix
                L[row][col] = (mat[row][col] / pivot * -1)*-1

        mat = mul_matrix(elem_mat, mat)

    return "L = {} \nU = {}".format(L, mat)


# return the maximum norm of matrix
def norm(mat):
    size = len(mat)
    max_row = 0
    for row in range(size):
        sum_row = 0
        for col in range(size):
            sum_row += abs(mat[row][col])
        if sum_row > max_row:
            max_row = sum_row
    return max_row


# returns the result of Ax=b
def part1(A, b):
    inverseMat = inverse(A)
    x = mul_matrix_wVector(inverseMat, b)
    return x


def main():
    #  Part 1 - The size of the matrix is less than 4
    A = [[2, 4, 6], [3, 0, 6], [4, 6, 8]]
    b = [16, 15, 12]

    print("The result of Ax=b is {}".format(part1(A, b)))
    print("cond = {}".format(norm(A)*norm(inverse(A))))

    #  Part 2 - The matrix size is equal or greater than 4

    B = [[1, -1, -2, 1, 1], [2, -3, -5, 2, 1], [-1, 3, 5, 1, 2], [1, 0, -2, 2, 1], [1, 5, 3, -1, 1]]

    print(LU(B))

main()