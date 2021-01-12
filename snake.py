
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    # The code here is going to determine what should happen when we initialize a new snake object
    def __init__(self):
        # below we create a new attribute for our class
        self.segments = []
        # We create a snake:
        self.create_snake()
        self.head = self.segments[0]


    # CREATING SNAKE (2 functions)
    def create_snake(self):
        for position in STARTING_POSITIONS:
            # we are calling the function and passing there the position that we are looping through
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Creating a snake extend function
    def extend(self):
        # we are using the list of segments and counting from the end of list to get the last one segment of the snake
        # after we are going to hold segment's position using a method of Turtle class
        # then we add the new_segment to the same position as the last segment
        self.add_segment(self.segments[-1].position())




    # Creating another method for snake class
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # if the current heading is pointed down it can't move up
        # because the snake can't go backword
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)





