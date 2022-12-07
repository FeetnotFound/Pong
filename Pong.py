import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)

# Score
s_a = 0
s_b = 0

# sounds

#Border
b_p = turtle.Turtle()
b_p.speed(0)
b_p.color("white")
b_p.penup()
b_p.setposition(-300, -300)
b_p.pensize(3)
b_p.pendown()
for side in range(4):
    b_p.fd(600)
    b_p.lt(90)
b_p.hideturtle()



# Paddle A
p_a = turtle.Turtle()
p_a.speed(0)
p_a.shape("square")
p_a.shapesize(stretch_wid=3, stretch_len=0.7)
p_a.color("white")
p_a.penup()
p_a.goto(-270,0)


# Paddle B
p_b = turtle.Turtle()
p_b.speed(0)
p_b.shape("square")
p_b.shapesize(stretch_wid=3, stretch_len=0.7)
p_b.color("white")
p_b.penup()
p_b.goto(270,0)


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.shapesize(stretch_wid=0.9, stretch_len=0.9)
ball.goto(0,0)
ball.dx = -0.3
ball.dy = -0.3


# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle
pen.goto(0, 270)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 12, "normal"))



def p_a_up():
    y = p_a.ycor()
    y += 15
    p_a.sety(y)

def p_a_down():
    y = p_a.ycor()
    y -= 15
    p_a.sety(y)

def p_b_up():
    y = p_b.ycor()
    y += 1.3
    p_b.sety(y)

def p_b_down():
    y =  p_b.ycor()
    y -= 1.3
    p_b.sety(y)


wn.listen()
wn.onkeypress(p_a_up, "w")
wn.onkeypress(p_a_down, "s")
wn.onkeypress(p_b_up, "Up")
wn.onkeypress(p_b_down, "Down")










while True:
    wn.update()

    # ball movement

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # border

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("wall.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("wall.wav", winsound.SND_ASYNC)
    
    if ball.xcor() > 300:
        ball.goto(0, 0)
        ball.dx *= -1
        s_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(s_a, s_b), align="center", font=("Courier", 16, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        


    if ball.xcor() < -300:
        ball.goto(0, 0)
        ball.dx *= -1
        s_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(s_a, s_b), align="center", font=("Courier", 16, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        


    # b and p
     
    if ball.xcor() > 260 and ball.xcor() < 270 and(ball.ycor() < p_b.ycor() + 40 and ball.ycor() > p_b.ycor() -50 ):
        ball.setx(260)
        ball.dx *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -260 and ball.xcor() > -270 and (ball.ycor() < p_a.ycor() + 40 and ball.ycor() > p_a.ycor() -50 ):
        ball.setx(-260)
        ball.dx *= -1  
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if p_b.ycor() < ball.ycor() and abs(p_b.ycor() - ball.ycor()) > 10:
        p_b_up()

    elif p_b.ycor() > ball.ycor()and abs(p_b.ycor() - ball.ycor()) > 10:
        p_b_down()