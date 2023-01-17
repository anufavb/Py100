from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forwards():
    turtle.forward(10)

def move_backwards():
    turtle.backward(10)

def turn_left():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)

def turn_right():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()