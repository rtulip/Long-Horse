import numpy as np

class Board:
	
	def __init__(self, width, height,food,body,enemies,health = 100):
		self.dimension = (width,height)
		self.width = width
		self.height = height
		self.food = food
		self.body = body
		self.enemies = enemies
		whip = np.zeros((width,height,2), dtype = object)

		for snack in food:
			whip[snack[0],snack[1]] = (-1,0)

		badboys = 1
		for baddy in enemies:
			badboys += 1
			thiccness = 0
			for baddy_bit in baddy:
				whip[baddy_bit[0],baddy_bit[1]] = (badboys+thiccness,1)
				thiccness = thiccness + 10

		thiccness = 1
		for bit in body:
			whip[bit[0],bit[1]] = (thiccness,1)
			thiccness = thiccness + 10
		
		self.board = whip

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

	

