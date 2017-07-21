from flood_fill import Board, flood_fill
from collections import deque

board=Board(1000,720)
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
MY_SET={(start_y, start_x)}

while len(QUEUE):
	y, x = QUEUE.pop()
	if board.board[y][x] == 'X':
		continue
	board.board[y][x] = 'X'
	QUEUE.appendleft((y+1, x))
	QUEUE.appendleft((y-1, x))
	QUEUE.appendleft((y, x+1))
	QUEUE.appendleft((y, x-1))


board=Board(1000,720)
board.create_square_object()
starting_y, starting_x = 10, 15


while len(MY_SET):
	y, x = MY_SET.pop()
	if board.board[y][x] == 'X':
		continue
	board.board[y][x] = 'X'
	MY_SET.add((y+1, x))
	MY_SET.add((y-1, x))
	MY_SET.add((y, x+1))
	MY_SET.add((y, x-1))


