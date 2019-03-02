import cloned.pypaths.pypaths.astar
States = {"Passive", "Hungry", "Hunter"}



def out_of_bounds(coords,board):
    x,y = coords
        if x < 0 or x > width -1:
            return True
        if y < 0 or y > height -1:
            return True
        else:
            return False

def is_safe(coords,board):
    x,y = coords
    identity, weight = board[x][y]
    if(not out_of_bounds(coords) and weight == 0):
        return True
    else:
        return False

def get_neighbours(coords,board):
    x,y = coords
    neighbours = []
    if(is_safe([x+1,y])):
        neighbours.append((x+1,y))
    if(is_safe([x-1,y])):
        neighbours.append((x-1,y))
    if(is_safe([x,y-1])):
        neighbours.append((x,y-1))
    if(is_safe([x,y+1])):
        neighbours.append((x,y+1))    
    return neighbours



def a_star(board,start,finish):
    start_x, start_y = start
    finish_x, finish_y = finish

    finder = astar.pathfinder(neighbors= get_neighbours)
    path = finder((start_x,start_y), (finish_x, finish_y))
    









