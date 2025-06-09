import random

def read(fname):
    matrix = []
    with open(fname) as f:
        for line in f:
            matrix.append(list(line.strip()))
    return matrix

def print_board(matrix):
    for r in matrix:
        print(" ".join(r))
    print()

def write(fname, matrix):
    with open(fname, 'w') as f:
        for r in matrix:
            f.write("".join(r) + "\n")

def full(matrix):
    for r in matrix:
        for el in r:
            if el == "-":
                return False
    return True

def check_win(matrix):
    for r in matrix:
        if r[0] != "-" and r[0] == r[1] == r[2]:
            return True
    for c in range(3):
        if matrix[0][c] != "-" and matrix[0][c] == matrix[1][c] == matrix[2][c]:
            return True
    if matrix[0][0] != '-' and matrix[0][0] == matrix[1][1] == matrix[2][2]:
        return True
    if matrix[0][2] != '-' and matrix[0][2] == matrix[1][1] == matrix[2][0]:
        return True
    return False

def get_empty_cells(matrix):
    return [(r, c) for r in range(3) for c in range(3) if matrix[r][c] == "-"]

def play_game(fname):
    matrix = read(fname)
    while not full(matrix):
        print_board(matrix)

        user = 'X'
        row = int(input('enter row (0-2): '))
        col = int(input('enter col (0-2): '))

        if matrix[row][col] == '-':
            matrix[row][col] = user
            write(fname, matrix)
        else:
            print('cell is filled')
            continue

        if check_win(matrix):
            print_board(matrix)
            print('user wins!')
            break

        if full(matrix):
            break

        print("computer's turn (O):")
        empty_cells = get_empty_cells(matrix)
        if empty_cells:
            r, c = random.choice(empty_cells)
            matrix[r][c] = 'O'
            write(fname, matrix)

        if check_win(matrix):
            print_board(matrix)
            print('computer wins!')
            break

    if not check_win(matrix):
        print_board(matrix)
        print('game over! draw')

with open('../works/board', 'w') as f:
    f.write("---\n" * 3)

play_game('board')
