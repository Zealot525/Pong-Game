from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,coordinate):
        super().__init__()
        self.color("white")
        self.score = 0
        self.pu()
        self.hideturtle()
        self.goto(coordinate)
        self.write(f"{self.score}", False, align="center", font=("Glacial", 45, "normal") )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False, align="center", font=("Glacial", 45, "normal") )

    def winner(self, winner):
        self.write(f"The winner is {winner}!", False,align="center",font=("Garamond", 45, "normal"))