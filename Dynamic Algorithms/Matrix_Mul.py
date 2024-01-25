def MatrixMultiplication(mat, i, j):

    arr = [[-1 for i in range(len(mat))] for j in range(len(mat))]

    if i == j:
        return 0

    if arr[i][j] != -1:
        return arr[i][j]

    arr[i][j] = int('inf')

    for k in range(i, j):
        arr[i][j] = min(arr[i][j], MatrixMultiplication(mat, i, k) + MatrixMultiplication(mat, k+1, j) + mat[i-1]*mat[k]*mat[j])

    return arr[i][j]


mat = [2, 3, 4, 5]


print(MatrixMultiplication(mat, 1, len(mat)-1))