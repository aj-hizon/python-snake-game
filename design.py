from turtle import Turtle

class Design(Turtle):
    def __init__(self, goto, text:str, font:tuple):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(goto)
        self.write(arg = text, align = "center", font = ("Arial", 10, "bold"))
        