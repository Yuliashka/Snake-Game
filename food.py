
from turtle import Turtle
import random

# we want this Food class to inherit from the Turtle class, so it will have all the capapibilities from
# the turtle class, but also some specific things that we want


class Food(Turtle):
    # creating initializer for this class
    def __init__(self):
        # we inherit things from the super class:
        super().__init__()
        # below we are using methods from Turtle class:
        self.shape("circle")
        self.penup()
        # normal sise is 20x20, we want to stretch the length and the width for 0.5 so we have 10x10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        # call the method refresh so the food goes in random location
        self.refresh()

    def refresh(self):
        # our screen is 600x600
        # we want to place our food from -280 to 280 in coordinates:
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        # telling our food to go to random_y and random_x:
        self.goto(random_x, random_y)

# All this methods will happen as soon as we create a new object
# This food object we initialize in main.py

