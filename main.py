from turtle import Screen
from baton import Baton
from ball import Ball
import time
from score import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.listen()
screen.tracer(0)

baton_right = Baton((370,0))
screen.onkeypress(baton_right.up, "Up")
screen.onkeypress(baton_right.down, "Down")


baton_left = Baton((-370,0))
screen.onkeypress(baton_left.up, "w")
screen.onkeypress(baton_left.down, "s")

ball = Ball()

left_score = Scoreboard((-150, 200))
right_score = Scoreboard((150, 200))

game_end = False
while not game_end:
    screen.update() 
    time.sleep(ball.ball_speed)
    ball.move()
    # Check for wall collision
    if  ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    # Check for baton collision
    if  ball.distance(baton_right) < 50 and ball.xcor() > 340 or ball.distance(baton_left) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    # check for scoring
    if ball.xcor() < -400:
        ball.restart_again()
        right_score.increase_score()
    elif ball.xcor() > 400:
        ball.restart_again()
        left_score.increase_score()

    if left_score.score == 3 or right_score.score == 3:
        if left_score.score > right_score.score:
            left_score.goto(0,0)
            left_score.write(f"The Left player is the winner!", False,align="center",font=("Garamond", 45, "normal"))
        elif left_score.score < right_score.score: 
            right_score.goto(0,0)
            right_score.write(f"The Right player is the winner!", False,align="center",font=("Garamond", 45, "normal"))
        game_end = True

screen.exitonclick()