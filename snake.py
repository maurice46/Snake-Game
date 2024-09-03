import turtle
import random
import time

# screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
# turtle operates with pendown state by default
# using penup() will stop drawing when turtle is moved
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,0)

# scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

# variables for the game
score = 0
high_score = 0
delay = 0.11

# create a list of segments
segments = []

# create a function for moving the snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# create a function to listen to the keyboard
def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"


screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

while True:
    screen.update()

    # Check for a collision with the border
    if (head.xcor() > 290 or head.xcor() < -290 or 
            head.ycor() > 255 or head.ycor() < -290):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop" 

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Update the score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), 
                  align="center", font=("Courier", 24, "normal"))


    # Move the snake
    move()

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a new random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 250)
        food.goto(x, y)

        # Add a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Update the score
        score += 1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score),
                  align="center", font=("Courier", 24, "normal"))

    # Move the segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Check for collisions with the segments
    for segment in segments[1:]:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Update the score
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score),
                      align="center", font=("Courier", 24, "normal"))

    # Delay the game loop
    time.sleep(delay)