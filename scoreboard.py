from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.pu()
        self.goto(-280,260)
        self.level = 1
        self.update_level()


    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.clear()
        self.write("GAME OVER!", font=FONT)

