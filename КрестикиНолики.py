def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]

    for col in range(3):
        if len(set(row[col] for row in board)) == 1 and board[0][col] != ' ':
            return board[0][col]

    if len(set(board[i][i] for i in range(3))) == 1 and board[0][0] != ' ':
        return board[0][0]

    if len(set(board[i][2 - i] for i in range(3))) == 1 and board[0][2] != ' ':
        return board[0][2]

    return None


def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = current_player
            winner = check_winner(board)

            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")


if __name__ == "__main__":
    tic_tac_toe()
