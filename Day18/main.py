from turtle import Turtle, Screen, colormode
import random
import colorgram

turtle = Turtle()

colormode(255)
def randomcolor():
    turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
def turtlecolorrgb(r, g, b):
    turtle.color(r, g, b)

turtle.speed("fastest")

'''
turtle.shape("turtle")
turtle.color("green")
turtle.left(90)
for _ in range(4):
    turtle.left(90)
    turtle.forward(100)

turtle.right(90)

for _ in range(15):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

for noOfSides in range(3, 11):
    randomcolor()
    angle = 360 / noOfSides
    for _ in range(noOfSides):
        turtle.forward(100)
        turtle.right(angle)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
turtle.pensize(10)

for _ in range(200):
    #turtle.color(random.choice(colours))
    randomcolor()
    turtle.forward(30)
    turtle.setheading(random.choice(directions))

noOfCircles = 50
turtle.setheading(90)
for _ in range(noOfCircles):
    randomcolor()
    turtle.circle(100)
    turtle.left(360/noOfCircles)

rgb_colors = []
colors = colorgram.extract('Day18/image.jpg', 20)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    rgb_colors.append(rgb)
print(rgb_colors)
'''
colorlist = [(215, 166, 17), (230, 239, 234), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42)]
turtle.hideturtle()
turtle.penup()
for i in range(10):
    for j in range(10):
        turtle.setpos(i*50, j*50)
        #turtle.color(random.choice(colorlist))
        #turtle.begin_fill()
        #turtle.circle(10)
        turtle.dot(20, random.choice(colorlist))
        #turtle.end_fill()

screen = Screen()
screen.exitonclick() 