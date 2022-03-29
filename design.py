from turtle import Turtle

class Design(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, -270)
        self.write(f"SNAKE GAME", align = "center", font = ("Arial", 10, "bold"))