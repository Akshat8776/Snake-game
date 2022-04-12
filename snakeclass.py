from tkinter import ttk
import turtle as t
import tkinter as tk
STP=[(0,0),(-20,0),(-40,0)]
MOVEDIS=20
class Snakeclass:
    
    def __init__(self):
        super().__init__()
        self.snake=[]
        self.create_snake()
        self.head=self.snake[0]
        
    def create_snake(self):
        for p in STP:
            s1=t.Turtle("square")
            s1.color("white")
            s1.penup()
            s1.goto(p)
            self.snake.append(s1)
            
    def eat(self):
        s1=t.Turtle("square")
        s1.color("white")
        s1.penup()
        p=self.head.xcor()
        q=self.head.ycor()
        s1.goto(p,q)
        self.snake.append(s1)
    
    def move(self):
        for i in range(len(self.snake)-1,0,-1):
            newx=self.snake[i-1].xcor()
            newy=self.snake[i-1].ycor()
            self.snake[i].goto(newx,newy)
        self.snake[0].forward(MOVEDIS) 

    def touchedge(self):
        x=self.head.xcor()
        y=self.head.ycor()
        if(x>300 or x<-300 or y<-300 or y>300):
            return True
    
    def up(self):
        if self.snake[0].heading()!=270:
            self.snake[0].setheading(90)
            
    
    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    
    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    
    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)
            
    def collision(self):
        for i in range(1,len(self.snake)):
            if self.head.distance(self.snake[i])<10:
                return False
        return True
    
    def popupmsg(self):
        root=tk.Tk()
        root.title("Game Over")
        msg="HIh     ello "
        label=ttk.Label(root,text=msg)
        label.pack(side="top",fill="x",pady=30)
        B1=tk.Button(root,text="Okay",command=root.destroy)
        B1.pack()
        t.Screen().mainloop()