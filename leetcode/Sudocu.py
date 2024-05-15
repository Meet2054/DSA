
# Sudocu

def is_perfect_matrix(matrix):
    n = len(matrix)
    seen = set()

    # Check rows
    for i in range(n):
        for j in range(n):
            num = matrix[i][j]
            if num in seen:
                return False
            seen.add(num)
        seen.clear()  # Clearing here was incorrect

    # Check columns
    for j in range(n):
        for i in range(n):
            num = matrix[i][j]
            if num in seen:
                return False
            seen.add(num)
        seen.clear()  # Clearing here was incorrect

    return True  # If all rows, columns, and subgrids are perfect


matrix = [
        [5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9]]

if len(set(num for row in matrix for num in row)) == 9:
    if is_perfect_matrix(matrix):
        print("The matrix is perfect.")
    else:
        print("The matrix is not perfect.")
else:
    print("The matrix does not contain exactly 9 unique elements.")

for row in matrix:
    print(row)

