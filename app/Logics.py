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
    if(not out_of_bounds(coords,board) and board.getBoard()[x][y][1] == 0):
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

#Retrurns a* path from one node to another
def a_star(board,start,finish):
    start_x, start_y = start
    finish_x, finish_y = finish

    finder = astar.pathfinder(neighbors= get_neighbours_builder(board))
    path = finder((start_x,start_y), (finish_x, finish_y))
    return path
'''
    TODO: 
        - Fix Problems with origin
        - Fix Problems with out of bounds index on food[0]
        
'''
#Use a* path to determine next move
def calc_move(board,path):
    print(path)
    next_coord = path[1][1]
    print(next_coord[0])
    print(next_coord[1])
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







