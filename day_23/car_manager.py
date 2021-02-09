from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    def __init__(self):
        self.cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
        
    def generate_car(self):
        random_chance=random.randint(1,6)
        if random_chance == 1:
            car=Turtle()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            y_coordinate=random.randint(-200,250)
            car.goto(300,y_coordinate)
            self.cars.append(car)
        
    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)
    
    def increase_speed(self):
        self.car_speed+=MOVE_INCREMENT