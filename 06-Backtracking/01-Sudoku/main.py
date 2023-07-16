def solve_sudoku(board):
    if not find_empty_location(board):
        return True

    row, col = find_empty_location(board)
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Backtrack

    return False


def find_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None


def is_safe(board, row, col, num):
    for i in range(9):
        if (
            board[row][i] == num or
            board[i][col] == num or
            board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num
        ):
            return False
    return True


def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))


# Example usage
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(board):
    print("Sudoku solved:")
    print_board(board)
else:
    print("No solution exists.")