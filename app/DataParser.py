

class DataParser:
    def __init__(self, data):
        width, height, food, body, enemies, health = process_data(self,data)

    def process_data(self, data):
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
                for e in s.get("body"):
                    x = e.get("x")
                    y = e.get("y")
                    enemies.append((x,y))

        return width,height, food, body, enemies, health

    def printer(food,body,enemies,health):
        #simple printer that prints to heroku logs
        #useful for debugging 

        print("Food: ",food)
        print("Body: ",body)
        print("Enemies: ",enemies)
        print("Health: ",health)

    def getWidth():
        return width
    
