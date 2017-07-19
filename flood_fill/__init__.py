import copy

class Board:
	
	def __init__(self, width=50, height=30, character='X'):
		self.width = width
		self.height = height
		self.character = character
		self.init_board()

	def init_board(self):
		self._top_row = list(self.character*self.width)
		self._bottom_row = self._top_row
		middle_row = list(self.character + ' '*(self.width-2) + self.character)
		middle_row_array = [copy.deepcopy(middle_row) for _ in range(self.height)]
		self.board = [self._top_row] + middle_row_array + [self._bottom_row]
	
	def print_board(self):
		print('\n')
		for row in self.board:
			print(''.join(row))
		print('\n')
	
	def create_square_object(self):
		start_left_corner= int(self.width/2), int(self.height/2)
		size=int(self.height/3)
		start_x, start_y = start_left_corner
		
		self.board[start_y][start_x] = self.character
		self.board[start_y+size][start_x+size] = self.character
		
		for i in range(size):
			# print('start_y: %s, start_x: %s' % (start_y + i, start_x + i))
			self.board[start_y][start_x+i] = self.character
			self.board[start_y+i][start_x] = self.character
			self.board[start_y+size][start_x+i] = self.character
			self.board[start_y+i][start_x+size] = self.character


def flood_fill(y, x, board):
	if board.board[y][x] == 'X':
		return
	# print('X: %s, Y: %s' % (x,y))
	board.board[y][x] = 'X'
	flood_fill(y+1, x, board)
	flood_fill(y-1, x, board)
	flood_fill(y, x+1, board)
	flood_fill(y, x-1, board)