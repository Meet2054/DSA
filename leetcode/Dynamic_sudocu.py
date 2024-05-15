def is_perfect_matrix(matrix):
    n = len(matrix)
    seen = set()

    # Check rows
    for i in range(n):
        for j in range(n):
            num = matrix[i][j]
            if num in seen and num != 0:
                return False
            seen.add(num)

    # Check columns
    for j in range(n):
        for i in range(n):
            num = matrix[i][j]
            if num in seen and num != 0:
                return False
            seen.add(num)

    return True


def matrix_create():
    n = 9
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    q = 1
    while q <= 81:
        input_str = input("Enter three integer values separated by spaces (value i j): ")
        values = input_str.split()

        # Checking if exactly three values were entered
        if len(values) != 3:
            print("Please enter exactly three values separated by spaces.")
            continue

        try:
            val = int(values[0])
            i = int(values[1])
            j = int(values[2])

            if i < 0 or i >= n or j < 0 or j >= n:
                print("Indices out of range.")
                continue
            # Check if the value repeats in the same row or column
            if val in matrix[i] or val in [matrix[x][j] for x in range(n)]:
                print("Value", val, "already exists in the same row or column.")
                continue

            if matrix[i][j] == 0:
                matrix[i][j] = val
                print("Value", val, "successfully assigned at position (", i, ",", j, ")")
                q += 1
            else:
                print("Position (", i, ",", j, ") is already occupied.")


            if q == 82:
                # Check for perfect matrix only after all cells are filled
                if is_perfect_matrix(matrix):
                    print("The matrix is perfect.")
                else:
                    print("The matrix is not perfect.")

            for row in matrix:
                print(row)
        except ValueError:
            print("Please enter integer values only.")


matrix_create()

