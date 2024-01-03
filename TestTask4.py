matr = [[1, 2, 3],
        [4, 5, 6],
        [2, 5, 9],
        [8, 9, 8]]

def transpose_matrix(matrix):
    transposed_matrix = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i] = matrix[i][j]
    for i in range(len(transposed_matrix)):
        print(transposed_matrix[i])
    print('Размер исходной матрицы:', len(matrix), 'x', len(matrix[0]))
    print('Размер транспонированной матрицы:', len(transposed_matrix), 'x', len(transposed_matrix[0]))

transpose_matrix(matr)