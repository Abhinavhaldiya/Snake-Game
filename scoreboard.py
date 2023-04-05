from turtle import Turtle
ALIGNMENT="center"
FONT=('Arial', 15, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("C:\\Users\\Abhinav Kumar\\OneDrive\\Desktop\\Python Programming\\Intermediate\\Projects\\Project 5 Snake\\data.txt") as file:
            self.high_score=int(file.read())
        self.color("white")
        self.speed(0)
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("C:\\Users\\Abhinav Kumar\\OneDrive\\Desktop\\Python Programming\\Intermediate\\Projects\\Project 5 Snake\\data.txt",mode="w") as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()