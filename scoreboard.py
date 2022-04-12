from turtle import Turtle
import turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("blue")
        self.penup()
        self.goto(0,270)
        self.high=self.highscore()
        self.write(f"Score : {self.score} High score : {self.high}",move=False,align="center",font=("Arial",20,"bold"))
        self.hideturtle()
        
    def sc_move(self):
        x=self.xcor()
        if(x>=240):
            x=-250
        x+=5
        self.goto(x,270)
        self.clear()
        self.write(f"Score : {self.score} High score : {self.high}",move=False,align="center",font=("Arial",20,"bold"))
    
    def inc_score(self):
        self.clear()
        self.score+=1
        if self.score>self.high:
            self.writehighscore(self.score)
        self.write(f"Score : {self.score} High score : {self.high}",move=False,align="center",font=("Arial",20,"bold"))
        
    def highscore(self):
        with  open("highscore.txt") as file:
            num=int(file.read())
            return num
        
    def writehighscore(self,n):
        with  open("highscore.txt",mode="w") as file:
            strn=str(n)
            self.high=n
            file.write(strn)
