import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player=Player()
screen.listen()
screen.onkey(player.up,"Up")

car_manager=CarManager()
scoreboard=Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move_cars()
    
    #Detect collision
    for car in car_manager.cars:
       if car.distance(player) < 20:
           game_is_on=False
           scoreboard.game_over()
           
    #Detect success crossing
    if player.has_crossed():
        player.start()
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()