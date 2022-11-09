# pygame project 1
# pingpong
# self-learn from youtube in vscode


import turtle

wn = turtle.Screen()
wn.title("First pygame project")
wn.bgcolor("pink")
wn.setup(width=800,height=600)
wn.tracer(0)



# Score
score_a = 0
score_b = 0

# Racket left (racket a)
racket_a = turtle.Turtle()
racket_a.speed(0)
racket_a.shape("square")
racket_a.color("white")
racket_a.shapesize(stretch_wid=6, stretch_len=1)
racket_a.penup()
racket_a.goto(-350,0)



# Racket Right (racket b)
racket_b = turtle.Turtle()
racket_b.speed(0)
racket_b.shape("square")
racket_b.color("white")
racket_b.shapesize(stretch_wid=6, stretch_len=1)
racket_b.penup()
racket_b.goto(350,0)




# Pingpong (Ball)
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = -0.7

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, -285)
pen.write("Player A : 0  Player B : 0", align="center", font=("Courier",24, "normal"))



# Function
def racket_a_up():
    y = racket_a.ycor()
    y += 20
    racket_a.sety(y)

def racket_a_down():
    y = racket_a.ycor()
    y -= 20
    racket_a.sety(y)
    
def racket_b_up():
    y = racket_b.ycor()
    y += 20
    racket_b.sety(y)

def racket_b_down():
    y = racket_b.ycor()
    y -= 20
    racket_b.sety(y)
    


# Keyboard binding
wn.listen()
wn.onkeypress(racket_a_up, "w")
wn.onkeypress(racket_a_down, "s")
wn.onkeypress(racket_b_up, "Up")
wn.onkeypress(racket_b_down, "Down")



# main game loop
while True:
    wn.update()
    
    # Move the pingpong ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    
    # Top and Bottom
    if  ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if  ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    # Left and Right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        
    # racket and ball collisions
    if ball.xcor() < -340 and ball.ycor() < racket_a.ycor() + 50 and ball.ycor() > racket_a.ycor() - 50:
        ball.dx *= -1 
    
    elif ball.xcor() > 340 and ball.ycor() < racket_b.ycor() + 50 and ball.ycor() > racket_b.ycor() - 50:
        ball.dx *= -1
