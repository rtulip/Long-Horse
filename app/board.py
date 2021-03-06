import numpy as np

class Board:
	
	def default_food_fcn(whip, food, dimension):
		for snack in food:
			whip[snack[0],snack[1]] = (-1,-1)
			if(snack[0] > 0):
				whip[snack[0]-1,snack[1]][1] = whip[snack[0]-1,snack[1]][1] - .5
			if(snack[0] < dimension[0]-1):
				whip[snack[0]+1,snack[1]][1] = whip[snack[0]+1,snack[1]][1] - .5 
			if(snack[1] > 0):
				whip[snack[0],snack[1]-1][1] = whip[snack[0],snack[1]-1][1] - .5
			if(snack[1] < dimension[1]-1):
				whip[snack[0],snack[1]+1][1] = whip[snack[0],snack[1]+1][1] - .5

			if(snack[0] > 1):
				whip[snack[0]-2,snack[1]][1] = whip[snack[0]-2,snack[1]][1] - .25
			if(snack[0] < dimension[0]-2):
				whip[snack[0]+2,snack[1]][1] = whip[snack[0]+2,snack[1]][1] - .25
			if(snack[1] > 1):
				whip[snack[0],snack[1]-2][1] = whip[snack[0],snack[1]-2][1] - .25
			if(snack[1] < dimension[1]-2):
				whip[snack[0],snack[1]+2][1] = whip[snack[0],snack[1]+2][1] - .25

		return whip

	def default_snake_fcn(whip, enemies, dimension, body):
		try:
			if (whip == None):
				print "WHIP == NONE"				
				return  np.zeros((dimension[0],dimension[1],2), dtype = object)
		except:
			if (whip.any() == None):
				print "SOME OF WHIP == NONE"
				return  np.zeros((dimension[0],dimension[1],2), dtype = object)
					
		badboys = 1
		for baddy in enemies:
			badboys += 1
			thiccness = 0
			head = baddy[0]
			neck = baddy[1]
			d = (head[0]-neck[0],head[1]-neck[1])
			m1 = (head[0]+d[0],head[1]+d[1])
			m2 = (head[0]+d[1],head[1]+d[0])
			m3 = (head[0]-d[1],head[1]-d[0])
			moves = (m1,m2,m3)

			for move in moves:
				if(move[0]>=0 and move[0]< dimension[0] and move[1]>=0 and move[1]< dimension[1] ):
					if(len(body)>len(baddy)):
						whip[move[0],move[1]][1] = whip[move[0],move[1]][1] - 1

					else:
						whip[move[0],move[1]][1] = whip[move[0],move[1]][1] + 1.5

			whip[head[0],head[1]] = (badboys+thiccness,1)
			for baddy_bit in baddy[1:]:
				thiccness = thiccness + 10

				whip[baddy_bit[0],baddy_bit[1]] = (badboys+thiccness,1)
				
				if(baddy_bit[0] > 0):
					whip[baddy_bit[0]-1,baddy_bit[1]][1] = whip[baddy_bit[0]-1,baddy_bit[1]][1] + .5
				if(baddy_bit[0] < dimension[0]-1):
					whip[baddy_bit[0]+1,baddy_bit[1]][1] = whip[baddy_bit[0]+1,baddy_bit[1]][1] + .5
				if(baddy_bit[1] > 0):
					whip[baddy_bit[0],baddy_bit[1]-1][1] = whip[baddy_bit[0],baddy_bit[1]-1][1] + .5
				if(baddy_bit[1] < dimension[1]-1):
					whip[baddy_bit[0],baddy_bit[1]+1][1] = whip[baddy_bit[0],baddy_bit[1]+1][1] + .5

				if(baddy_bit[0] > 1):
					whip[baddy_bit[0]-2,baddy_bit[1]][1] = whip[baddy_bit[0]-2,baddy_bit[1]][1] + .25
				if(baddy_bit[0] < dimension[0]-2):
					whip[baddy_bit[0]+2,baddy_bit[1]][1] = whip[baddy_bit[0]+2,baddy_bit[1]][1] + .25
				if(baddy_bit[1] > 1):
					whip[baddy_bit[0],baddy_bit[1]-2][1] = whip[baddy_bit[0],baddy_bit[1]-2][1] + .25
				if(baddy_bit[1] < dimension[0]-2):
					whip[baddy_bit[0],baddy_bit[1]+2][1] = whip[baddy_bit[0],baddy_bit[1]+2][1] + .25

		thiccness = 1
		for bit in body[:-1]:
			whip[bit[0],bit[1]] = (thiccness,10)
		
			if(bit[0] > 0):
				whip[bit[0]-1,bit[1]][1] = whip[bit[0]-1,bit[1]][1] + .5
			if(bit[0] < dimension[0]-1):
				whip[bit[0]+1,bit[1]][1] = whip[bit[0]+1,bit[1]][1] + .5
			if(bit[1] > 0):
				whip[bit[0],bit[1]-1][1] = whip[bit[0],bit[1]-1][1] + .5
			if(bit[1] < dimension[1]-1):
				whip[bit[0],bit[1]+1][1] = whip[bit[0],bit[1]+1][1] + .5

			if(bit[0] > 1):
				whip[bit[0]-2,bit[1]][1] = whip[bit[0]-2,bit[1]][1] + .25
			if(bit[0] < dimension[0]-2):
				whip[bit[0]+2,bit[1]][1] = whip[bit[0]+2,bit[1]][1] + .25
			if(bit[1] > 1):
				whip[bit[0],bit[1]-2][1] = whip[bit[0],bit[1]-2][1] + .25
			if(bit[1] < dimension[0]-2):
				whip[bit[0],bit[1]+2][1] = whip[bit[0],bit[1]+2][1] + .25

			thiccness = thiccness + 10
	
		
		return whip


	def __init__(self, width, height,food,body,enemies,health=100, food_weight_fcn = default_food_fcn, snake_weight_fcn= default_snake_fcn):
		self.dimension = (width,height)
		self.width = width
		self.height = height
		self.food = food
		self.body = body
		self.enemies = enemies
		whip = np.zeros((width,height,2), dtype = object)
		whip = food_weight_fcn(whip, self.food, self.dimension)
		whip = snake_weight_fcn(whip, self.enemies, self.dimension, self.body)	
	
		self.board = whip

	
	def getCost(self,x,y):
		return(self.board[x,y][1])

	def getBoard(self):
		return(self.board)
	
	def getDim(self):
		return(self.dimension)

	def numEnemies(self):
		return(len(self.enemies))

	def numFood(self):
		return(len(self.food))

	def mySize(self):
		return(len(self.body))

	def getEnemies(self):
		return(self.enemies)
	
	def getBody(self):
		return(self.body)


def test():
	width  = 10
	height = 10
	food = [(0,0),(4,4),(5,6),(7,3),(9,9)]
	body = [(8,8),(8,9)]
	enemies = [ [(2,1),(2,2)] , [(3,1),(3,2)] , [(4,1),(4,2),(4,3)] ]	

	b = Board(width,height,food,body,enemies)

	correct_board = [ [ [-1,0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0] ],
					  [ [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0] ],
					  [ [0, 0], [2, 1], [12,1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0] ],
					  [ [0, 0], [3, 1], [13,1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0] ],
					  [ [0, 0], [4, 1], [14,1], [24,1], [-1,0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0] ], 
					  [ [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [-1,0], [0, 0], [0, 0], [0, 0], [0, 0] ],
					  [ [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0] ],
 					  [ [0, 0], [0, 0], [0, 0], [-1,0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0] ],
		 			  [ [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 1], [11,1] ],
					  [ [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [-1,0] ] 
					]	

	assert b.width == width
	assert b.height == height
	assert b.food == food
	assert b.body == body
	assert b.enemies == enemies

	for row in range(b.height):
		for col in range(b.width):
			assert (b.getBoard()[row][col] == correct_board[row][col]).all
			#print(b.getCost(col,row),correct_board[row][col][1] )
			#try:
			#	assert (b.getCost(row,col) == correct_board[row][col][1])
			#except:
				#print row, col, b.getCost(row,col), correct_board[row][col][1]
			#	print('owch')

