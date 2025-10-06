def solve_sudoku(matrix):
    def is_valid(r, c, num):

        for i in range(4):
            if matrix[r][i] == num or matrix[i][c] == num:
                return False

        start_r, start_c = 2 * (r // 2), 2 * (c // 2)
        for i in range(start_r, start_r + 2):
            for j in range(start_c, start_c + 2):
                if matrix[i][j] == num:
                    return False
        return True

    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                for num in range(1, 5):
                    if is_valid(i, j, num):
                        matrix[i][j] = num
                        if solve_sudoku(matrix):
                            return True
                        matrix[i][j] = 0
                return False
    return True

matrix = [
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 1, 0, 0],
    [3, 0, 0, 4]
]
solve_sudoku(matrix)
for row in matrix:
    print(''.join(map(str, row)))
