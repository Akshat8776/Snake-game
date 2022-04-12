from asyncore import write
import turtle as t
import tkinter
from snakeclass import Snakeclass
from food import Food
from scoreboard import Scoreboard
import time
s=t.Screen()
s.setup(width=600,height=600)
s.bgcolor("black")
s.title("Akshat snake game")
s.tracer(0)
sna=Snakeclass()
food=Food()
scoreboard=Scoreboard()

s.listen()
s.onkey(sna.up, "Up")
s.onkey(sna.down, "Down")
s.onkey(sna.left, "Left")
s.onkey(sna.right, "Right")

play=True
while(play):
    s.update()
    time.sleep(0.3)
    sna.move()
    play=sna.collision()
    scoreboard.sc_move()
    if sna.head.distance(food) < 15:
        food.refresh()
        sna.eat()
        scoreboard.inc_score()
    if sna.touchedge():
        play=False
print(f"Your score is : {scoreboard.score}\nHigh score was : {scoreboard.high}")