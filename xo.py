def read_games(fname):
    with open(fname, 'r') as f:
        content = f.read().strip()
    games = {}
    parts = content.split('-game')
    for part in parts:
        if part.strip():
            header, *lines = part.strip().splitlines()
            game_number = header.strip('-')
            games[f'game{game_number}'] = lines
    return games

def horizontal_winner(board):
    for row in board:
        if len(set(row)) == 1 and row[0] in 'xo':
            return row[0]
    return None

def vertical_winner(board):
    for col in range(3):
        column = [board[row][col] for row in range(3)]
        if len(set(column)) == 1 and column[0] in 'xo':
            return column[0]
    return None

def get_winner(board):
    return horizontal_winner(board) or vertical_winner(board) or 'd'

def write_results(games, result_filename):
    with open(result_filename, 'w') as res_file:
        for game_name, board in games.items():
            winner = get_winner(board)
            res_file.write(f"{game_name} {winner}\n")

def print_game_boards(games):
    for game_name, board in games.items():
        print(f"{game_name}")
        for line in board:
            print(line)
        print()

games = read_games("xo")
print_game_boards(games)
write_results(games, "reso.txt")
