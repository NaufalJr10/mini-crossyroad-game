import time
from turtle import Turtle
import random
import player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.list_of_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        random_chance = random.randint(0, 6)

        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(320, random.randint(-250, 250))
            new_car.setheading(180)
            self.list_of_cars.append(new_car)

    def move_car(self):
        for each_car in self.list_of_cars:
            each_car.forward(self.car_speed)

    def increase_speed(self):
        for each_car in self.list_of_cars:
            self.car_speed += 0.25




































































