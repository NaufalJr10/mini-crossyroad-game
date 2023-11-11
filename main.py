
import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.make_car()
    cars.move_car()

    for each_car in cars.list_of_cars:
        if each_car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.check_top():
        player.go_to_start()
        cars.increase_speed()
        scoreboard.increase_level()


































screen.exitonclick()
