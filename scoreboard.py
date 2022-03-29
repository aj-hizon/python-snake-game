from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Arial", 15, "bold")

# --opening the file--
with open('snakeGame\data.txt') as high:
    score_high = high.read()
    print(score_high)
    

# --writing inside the file--
# with open('day-24-file-system\proku-statement.txt', mode="a") as file:
#     file.write("\nalaanyare")




class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(score_high)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score}        HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('snakeGame\data.txt', mode = 'w') as high:
                high.write(str(self.high_score))
        self.score = 0 
        
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



