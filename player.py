from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("cyan")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.fd(MOVE_DISTANCE)

    def go_down(self):
        self.bk(MOVE_DISTANCE)

    def check_top(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

