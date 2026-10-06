# Bài 20: Ma trận dạng list lồng nhau
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

n = len(matrix)
main_diag = 0
anti_diag = 0
for i in range(n):
    main_diag += matrix[i][i]
    anti_diag += matrix[i][n - 1 - i]

print("Tổng đường chéo chính:", main_diag)
print("Tổng đường chéo phụ:", anti_diag)

tuple_matrix = tuple(tuple(row) for row in matrix)
print("Tuple của tuple:", tuple_matrix)
