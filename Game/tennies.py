

import turtle as tr
import winsound

ground = tr.Screen()
ground.bgpic("Image - 3.png") #Tennies ground image
ground.setup(width=1.0, height=1.0) # To set full screen
ground.addshape("image -1.gif") #Right player imageq
ground.addshape("Image - 2.gif") #Left player image
ground.addshape("Image - 4.gif") #ball image

#Assign right player image and position it.
right_player = tr.Turtle()
right_player.penup()
right_player.shape("image -1.gif")
right_player.goto(400,-200)

# Assign left player image and position it.
left_player = tr.Turtle()
left_player.penup()
left_player.shape("Image - 2.gif")
left_player.goto(-400, 200)

leftpen = tr.Turtle()
leftpen.penup()
leftpen.hideturtle()
leftpen.goto(-350, 250)
leftpen.color("white")
leftpen.write("Left_Player Score: 0", font=("Courier", 14, "bold"))

rightpen = tr.Turtle()
rightpen.penup()
rightpen.hideturtle()
rightpen.goto(100, 250)
rightpen.color("white")
rightpen.write("Right_Player Score: 0", font=("Courier", 14, "bold"))

#Assign ball image and position it.
ball = tr.Turtle()
ball.penup()
ball.shape("Image - 4.gif")

#Assign the function for left player
def left_playerUp():
    y = left_player.ycor()
    left_player.sety(y+10)
def left_playerDown():
    y = left_player.ycor()
    left_player.sety(y-10)
def left_playerRight():
    x = left_player.xcor()
    left_player.setx(x+10)
def left_playerLeft():
    x = left_player.xcor()
    left_player.setx(x-10)

#Assign the function for right player
def right_playerUp():
    y = right_player.ycor()
    right_player.sety(y+10)
def right_playerDown():
    y = right_player.ycor()
    right_player.sety(y-10)
def right_playerRight():
    x = right_player.xcor()
    right_player.setx(x+10)
def right_playerLeft():
    x = right_player.xcor()
    right_player.setx(x-10)


# Safe quit function
def quit_game():
    tr.bye()  # Cleanly close the turtle graphics window

#Assign left player shortcut keys on keyboard
tr.listen()
tr.onkeypress(left_playerUp, "w")
tr.onkeypress(left_playerDown, "s")
tr.onkeypress(left_playerRight, "d")
tr.onkeypress(left_playerLeft, "a")

#Assign right player shortcut keys on keyboard
tr.onkeypress(right_playerUp, "Up")
tr.onkeypress(right_playerDown, "Down")
tr.onkeypress(right_playerRight, "Right")
tr.onkeypress(right_playerLeft, "Left")

tr.onkeypress(quit_game, "q")  # Press 'q' to quit safely

#ball varible
import time
dx = 5
dy = -5
leftscore = 0
rightscore = 0
# ball move
while True:
    x = ball.xcor()
    y = ball.ycor()
    ball.setpos(x+dx, y+dy)
    # if right_player.distance(ball) < 10:
    #     dx=-dx
    # if left_player.distance(ball) < 10:
        
    #     dx=-dx

    # Right player hit
    if abs(ball.xcor() - right_player.xcor()) < 40 and abs(ball.ycor() - right_player.ycor()) < 50:
        dx = -dx

# Left player hit
    if abs(ball.xcor() - left_player.xcor()) < 40 and abs(ball.ycor() - left_player.ycor()) < 50:
        dx = -dx
    
    if ball.ycor() < -280:
        dy=-dy
    if ball.ycor() > 280:
        dy=-dy
    if ball.xcor() < -450:
        ball.goto(0,0)
        rightscore += 1
        rightpen.clear()
        rightpen.write("Right_Player Score: {}".format(rightscore), font=("Courier", 14, "bold"))
        dx = 5
        dy = -5
    if ball.xcor() > 450:
        ball.goto(0,0)
        leftscore += 1
        leftpen.clear()
        leftpen.write("Left_Player Score: {}".format(leftscore), font=("Courier", 14, "bold"))
        dx = 5
        dy = -5

        # Check for winner
    if leftscore == 2 or rightscore == 2:
        center_pen = tr.Turtle()
        center_pen.hideturtle()
        center_pen.penup()
        center_pen.color("white")
        center_pen.goto(0, 0)
        
        winner = "Left Player" if leftscore == 5 else "Right Player"
        center_pen.write(f" {winner} is Winner\n GAME OVER", align="center", font=("Courier", 32, "bold"))
        #center_pen.write(f"GAME OVER\n", align="center", font=("Courier", 32, "bold"))
        time.sleep(5)
        center_pen.clear()

        # Optional sound
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)    

        # Reset everything
        leftscore = 0
        rightscore = 0
        leftpen.clear()
        rightpen.clear()
        leftpen.write("Left_Player Score: 0", font=("Courier", 14, "bold"))
        rightpen.write("Right_Player Score: 0", font=("Courier", 14, "bold"))
        ball.goto(0, 0)
        left_player.goto(-400, 200)
        right_player.goto(400, -200)
        dx = 5
        dy = -5


    time.sleep(0.01)  # slow down the ball movement



tr.done()