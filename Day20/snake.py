from turtle import Turtle 
SNAKEWIDTH = 20

class Snake:
    def __init__(self, snakelen = 3, snake = []):
        self.snakelen = snakelen
        self.snake = snake
        self.__create_snake()
        self.head = self.snake[0]
        
    def __create_snake(self):
        for _ in range(self.snakelen):
            segm = Turtle()
            segm.penup()
            segm.shape("square")
            segm.color("white")
            if len(self.snake) > 0:
                segm.setpos(self.snake[len(self.snake)-1].xcor() - SNAKEWIDTH, self.snake[len(self.snake)-1].ycor())
            self.snake.append(segm)

    def move(self):
        for segm_num in range(len(self.snake)-1, 0, -1):
            self.snake[segm_num].goto(self.snake[segm_num-1].position()) 
        self.head.forward(20)

    def __change_direction(self, dir):
        self.head.setheading(dir)

    def up(self):
        if(self.head.heading() != 270): self.__change_direction(90)
    def down(self):
        if(self.head.heading() != 90): self.__change_direction(270)
    def left(self):
        if(self.head.heading() != 0): self.__change_direction(180)
    def right(self):
        if(self.head.heading() != 180): self.__change_direction(0)


