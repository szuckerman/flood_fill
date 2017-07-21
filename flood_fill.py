from flood_fill import Board, flood_fill
from collections import deque

board=Board(25,15)
board.print_board()

board.create_square_object()

# Fill inside square
starting_y, starting_x = 10, 15

# Fill outside square
starting_y, starting_x = 2, 2

board.print_board()		

flood_fill(starting_y, starting_x, board)

board.print_board()



# Now done iteratively
start_y, start_x = 10, 10
QUEUE=deque([(start_y, start_x)])

while len(QUEUE):
	y, x = QUEUE.pop()
	if board.board[y][x] == 'X':
		continue
	board.board[y][x] = 'X'
	QUEUE.appendleft((y+1, x))
	QUEUE.appendleft((y-1, x))
	QUEUE.appendleft((y, x+1))
	QUEUE.appendleft((y, x-1))




