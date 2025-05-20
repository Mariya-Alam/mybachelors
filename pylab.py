def matrix_addition(matrix1, matrix2):

    # Check if inputs are valid matrices
    if not (is_matrix(matrix1) and is_matrix(matrix2)):
        raise TypeError("Both inputs must be matrices (list of lists or numpy arrays)")

    # Convert numpy arrays to lists for consistent processing
    if hasattr(matrix1, 'tolist'):
        matrix1 = matrix1.tolist()
    if hasattr(matrix2, 'tolist'):
        matrix2 = matrix2.tolist()

    # Check matrix dimensions
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    if rows1 != rows2 or cols1 != cols2:
        raise ValueError(f"Incompatible matrix dimensions: ({rows1}x{cols1}) and ({rows2}x{cols2})")

    # Perform element-wise addition
    result = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            try:
                row.append(matrix1[i][j] + matrix2[i][j])
            except TypeError:
                raise TypeError(f"Non-numeric element at position ({i},{j})")
        result.append(row)

    return result


def is_matrix(m):
    """Helper function to check if an object is a valid matrix."""
    if isinstance(m, list):
        if not m or not all(isinstance(row, list) for row in m):
            return False
        row_length = len(m[0])
        return all(len(row) == row_length for row in m)
    elif hasattr(m, 'shape'):  # For numpy arrays
        return len(m.shape) == 2
    return False


# Example usage:
if __name__ == "__main__":
    # Example 1: Basic usage with list of lists
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    print("Matrix A:")
    for row in A:
        print(row)

    print("\nMatrix B:")
    for row in B:
        print(row)

    C = matrix_addition(A, B)
    print("\nA + B:")
    for row in C:
        print(row)
