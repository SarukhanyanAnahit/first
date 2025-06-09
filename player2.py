def read(fname):
    matrix=[]
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
            f.write("".join(r)+"\n")

def full(matrix):
    for r in matrix:
        for el in r:
            if el=="-":
                return False
    return True

def check_win(matrix):
    for r in matrix:
        if r[0]!="-" and r[0]==r[1]==r[2]:
            return True

    for c in range(3):
        if matrix[0][c]!="-" and matrix[0][c]==matrix[1][c]==matrix[2][c]:
            return True

    if matrix[0][0]!='-' and matrix[0][0]==matrix[1][1]==matrix[2][2]:
        return True
    if matrix[0][2]!='-' and matrix[0][2]==matrix[1][1]==matrix[2][0]:
        return True
    return False

def play_game(fname):
    matrix=read(fname)
    while not full(matrix):
        print_board(matrix)
        symb=input('enter X or O: ').upper()
        if symb!= 'X' and symb!= 'O':
            print("invalid")
            continue

        row=int(input('enter row 0-2: '))
        col=int(input('enter col 0-2: '))

        if matrix[row][col]=='-':
            matrix[row][col]=symb
            write(fname, matrix)
        else:
            print('cell is filled')
            continue

        if check_win(matrix):
            print('win')
            print_board(matrix)
            break

    print('game over!')
play_game('board')
