def print_board(board):
    for i_row in range(5, -1, -1):
        row = "|"
        for i_column in range(7):
            if board[i_column][i_row] == 1:
                row += " X"
            elif board[i_column][i_row] == 2:
                row += " O"
            else:
                row += "  "
        row += " |"
        print(row)

    print("-----------------")
