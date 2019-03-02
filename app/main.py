import json
import os
import random
import bottle
from board import Board
from api import ping_response, start_response, move_response, end_response

def process_data(data):
    #Process JSON input into a more usable format
    food_data = data.get("board").get("food")
    snakes = data.get("board").get("snakes")
    health = data.get("you").get("health")
    width = data.get("board").get("width")
    height =  data.get("board").get("height")

    food = []
    enemies = []
    body = []

    for f in food_data:
        x = f.get("x")
        y = f.get("y")
        food.append((x,y))
    for s in snakes:
        if s.get("id") == data.get("you").get("id"):
            for b in s.get("body"):
                x = b.get("x")
                y = b.get("y")
                body.append((x,y))
        else:
            enemy_snake = []
            for e in s.get("body"):
                x = e.get("x")
                y = e.get("y")
                enemy_snake.append((x,y))
            enemies.append(enemy_snake)

    return width,height, food, body, enemies, health

def printer(food,body,enemies,health):
    #simple printer that prints to heroku logs
    #useful for debugging
    print("hello")

@bottle.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.io">https://docs.battlesnake.io</a>.
    '''

@bottle.route('/static/<path:path>')
def static(path):
    """
    Given a path, return the static file located relative
    to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/')

@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return ping_response()

@bottle.post('/start')
def start():
    data = bottle.request.json

    #Board height and width
    b_height = data.get("board").get("height")
    b_width = data.get("board").get("width")
    
    food = data.get("board").get("food")
    snakes = data.get("board").get("snakes")
    #print(json.dumps(data))

    color = "#00FF00"

    return start_response(color)


@bottle.post('/move')
def move():
    data = bottle.request.json

    directions = ['up', 'down', 'left', 'right']

    food = []
    body = []
    enemies = []
    health = -1

    #Process Data from JSON request
    #food,body,enemies stored as list of tuples containing x,y positions [(x,y)]
    #health is stored as an integer between 0-100
    width,height,food, body, enemies, health = process_data(data)
    print(enemies) 
    board = Board(width,height,food, body, enemies, health)
    direction = 'left'
    
    return move_response(direction)


@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    #print(json.dumps(data))

    return end_response()

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
