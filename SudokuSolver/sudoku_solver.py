from pprint import pprint

# FIND SOMEWHERE TO START/CONTINUE
def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c

    return None, None


# VALID GUESS?
def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False

    # REMEMBER THE RULES: A number must not be repeated in the row, column, or 3x3 square that it appears in

    row_vals = puzzle[row]
    if guess in row_vals:
        return False  # if we've repeated, then our guess is not valid!

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3  # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True


def solve_sudoku(puzzle):
    # Backtracking a list of lists (our puzzle where the inner lists are the rows)

    # GUESS
    row, col = find_next_empty(puzzle)

    # EDGE CASE (ALREADY COMPLETE)
    if row is None:  # this is true if our find_next_empty function returns None, None
        return True

    # PLEASE VALUES 1-9 in order checking validity of guess each time. If valid then place.
    for guess in range(1, 10):  # range(1, 10) is 1, 2, 3, ... 9
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True

        # NOT VALID, BACKTRACK AND TRY NEXT NUMBER
        puzzle[row][col] = 0

    # UNSOLVABLE
    return False


if __name__ == "__main__":
    example_board = [
        [0, 0, 6,   0, 0, 0,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        [7, 0, 0,   0, 4, 8,   0, 0, 6],
        
        [0, 7, 0,   0, 0, 1,   0, 0, 0],
        [0, 4, 0,   0, 0, 0,   0, 0, 9],
        [2, 0, 0,   0, 8, 0,   0, 5, 7],

        [5, 0, 0,   0, 0, 0,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 2, 0],
        [0, 0, 0,   0, 1, 0,   5, 4, 0],
    ]
    pprint(example_board)
    print(solve_sudoku(example_board))
pprint(example_board)
