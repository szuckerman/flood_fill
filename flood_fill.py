from flood_fill import Board, flood_fill

board=Board(25, 15)
board.print_board()

board.create_square_object()

# Fill inside square
starting_y, starting_x = 10, 15

# Fill outside square
starting_y, starting_x = 2, 2

board.print_board()

flood_fill(starting_y, starting_x, board)

board.print_board()

