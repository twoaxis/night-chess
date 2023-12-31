from pieces.Piece import Piece
from pieces.Blank import Blank

class Pawn(Piece):
	def __init__(self, x, y, color):
		if color == "W":
			super().__init__(x, y, "assets/w_p.png", color)
		else:
			super().__init__(x, y, "assets/b_p.png", color)
	def get_moves(self, data):
		moves = []
		if self.color == "W":
			if isinstance(data[self.x+1][self.y], Blank):
				moves.append([1, 0])
				if self.x == 1:
					if isinstance(data[self.x+2][self.y], Blank):
						moves.append([2, 0])
			if 0<= self.x +1 <=7 and 0<=self.y +1 <=7:
				if not isinstance(data[self.x+1][self.y+1],Blank) and data[self.x+1][self.y+1].color != "W":
					moves.append([1,1])
			if 0<= self.x +1 <=7 and 0<=self.y -1 <=7:
				if not isinstance(data[self.x+1][self.y-1],Blank) and data[self.x+1][self.y-1].color != "W":
					moves.append([1,-1])
			
		else:
			if isinstance(data[self.x-1][self.y],Blank):           
				moves.append([-1, 0])
				if self.x == 6:
					if isinstance(data[self.x-2][self.y], Blank):
						moves.append([-2, 0])
			if 0<= self.x - 1 <=7 and 0<=self.y +1 <=7:
				if not isinstance(data[self.x-1][self.y+1],Blank) and data[self.x-1][self.y+1].color == "W":
					moves.append([-1,1])
			if 0<= self.x - 1 <=7 and 0<=self.y - 1 <=7:
				if not isinstance(data[self.x-1][self.y-1],Blank) and data[self.x-1][self.y-1].color == "W":
					moves.append([-1,-1])
		return moves
