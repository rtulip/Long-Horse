from pypaths import astar
import board
import random
States = {"Passive", "Hungry", "Hunter"}


#Checks if coordinate is out of bounds of the gameboard
def out_of_bounds(coords,board):
    x,y = coords
    width,height = board.getDim()
    if x < 0 or x > width -1:
        return True
    if y < 0 or y > height -1:
        return True
    else:
        return False

#Checks if coordinate is out of bounds and admissable
#TODO: May need to be changed with weighting scheme
def is_safe(coords,board):
    x,y = coords
    if(not out_of_bounds(coords,board) and board.getBoard()[x][y][0] % 10 != 1 and board.getBoard()[x][y][1] < 1):
        return True
    else:
        return False

#Get neighbourhood (N,E,S,W) around a specific node
#Will only add valid neighbours
#Neighbourhood builder used to pass function into a star
def get_neighbours_builder(board):
    def get_neighbours(coords):
        x,y = coords
        neighbours = []
        if(is_safe(([x+1,y]),board)):
            neighbours.append((x+1,y))
        if(is_safe(([x-1,y]),board)):
            neighbours.append((x-1,y))
        if(is_safe(([x,y-1]),board)):
            neighbours.append((x,y-1))
        if(is_safe(([x,y+1]),board)):
            neighbours.append((x,y+1))

        return neighbours

    return get_neighbours

def costConstructor(board):
    def cost(a,b):
        scale = 11
        weight = board.getCost(b[0],b[1])
        return(scale*(1+weight))
    return cost

#Retrurns a* path from one node to another
def a_star(board,start,finish):
    start_x, start_y = start
    finish_x, finish_y = finish

    finder = astar.pathfinder(neighbors= get_neighbours_builder(board),cost = costConstructor(board))
    path = finder((start_x,start_y), (finish_x, finish_y))
    return path
'''
    TODO: 
        - Fix Problems with origin
        - Fix Problems with out of bounds index on food[0]
        
'''
#Use a* path to determine next move
def calc_move(board,path):
    path_coords = path[1]
    path_length = path[0]
    #next_coord = path[1][1]
    next_coord = path_coords[1]
    print(path_coords)
    print(path_length)

    body = board.getBody()
    head = body[0]
    head_x, head_y = head
    width, height = board.getDim()
    directions = []
    
    if next_coord[1] < head_y:
        directions.append("up")
    if next_coord[1] > head_y:
        directions.append("down")
    if next_coord[0] > head_x:
        directions.append("right")
    if next_coord[0] < head_x:
        directions.append("left")
    
    #Pick a random choice from viable options (for now)
    direction = random.choice(directions)
    return direction

def test():
	from board import Board	
	width  = 10
	height = 10
	food = [(0,0),(4,4),(5,6),(7,3),(9,9)]
	body = [(8,8),(8,9)]
	enemies = [ [(2,1),(2,2)] , [(3,1),(3,2)] , [(4,1),(4,2),(4,3)] ]	

	b = Board(width,height,food,body,enemies)

	assert out_of_bounds((-1, 5), b) == True
	assert out_of_bounds((5, -1), b) == True
	assert out_of_bounds((0 , 5), b) == False
	assert out_of_bounds((5,  0), b) == False
	assert out_of_bounds((5,  9), b) == False
	assert out_of_bounds((9,  5), b) == False
	assert out_of_bounds((10, 5), b) == True
	assert out_of_bounds((5, 10), b) == True

	assert is_safe((-1, 5), b) == False
	assert is_safe((5, -1), b) == False
	assert is_safe((0, 5), b)  == True
	assert is_safe((5, 0), b)  == True
	assert is_safe((5, 9), b)  == True
	assert is_safe((9, 5), b)  == True
	assert is_safe((10, 5), b) == False
	assert is_safe((5, 10), b) == False
	assert is_safe((2, 1), b)  == False
	assert is_safe((2, 2), b)  == False
	assert is_safe((3, 1), b)  == False
	assert is_safe((3, 2), b)  == False
	assert is_safe((4, 1), b)  == False
	assert is_safe((4, 2), b)  == False		
	assert is_safe((4, 3), b)  == False
	
	path = a_star(b, body[0], food[0])
	print(path)


	print(calc_move(b, path))






