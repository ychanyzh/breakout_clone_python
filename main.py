import PythonTurtle as turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turns off the screen updates

# Create the paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Create the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2  # Ball's x-axis speed
ball.dy = -2  # Ball's y-axis speed

# Create the bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]

for y in range(5):
    for x in range(8):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(colors[y])
        brick.penup()
        brick.goto(-350 + x * 100, 250 - y * 50)
        bricks.append(brick)

# Paddle movement functions
def move_paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 20
    paddle.setx(x)


def move_paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 20
    paddle.setx(x)


# Keyboard bindings
screen.listen()
screen.onkeypress(move_paddle_left, "Left")
screen.onkeypress(move_paddle_right, "Right")

# Game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 390:  # Right border
        ball.setx(390)
        ball.dx *= -1
    elif ball.xcor() < -390:  # Left border
        ball.setx(-390)
        ball.dx *= -1
    if ball.ycor() > 290:  # Top border
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:  # Bottom border
        ball.goto(0, 0)
        ball.dy *= -1

    # Paddle and ball collisions
    if (
        ball.ycor() < -240
        and paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50
        and ball.dy < 0
    ):
        ball.dy *= -1

    # Brick and ball collisions
    for brick in bricks:
        if (
            brick.distance(ball) < 30
            and brick.ycor() > ball.ycor()
            and ball.dy > 0
        ):
            brick.goto(1000, 1000)  # Move the brick off-screen
            ball.dy *= -1

    # Check if all bricks are broken
    if all(brick.ycor() > 1000 for brick in bricks):
        # Game over condition (You can add your own game over logic)
        break

# Exit the game
screen.onkeypress(screen.bye, "Escape")

# Start the game
screen.mainloop()
