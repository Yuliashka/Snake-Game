
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

# SETTING UP THE SCREEN:
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# to turn off the screen tracer
screen.tracer(0)

# CREATING A SNAKE OBJECT:
snake = Snake()

# CREATING A FOOD OBJECT:
food = Food()

# CREATING A SCORE OBJECT:
score = Score()

# CREATING A KEY CONTROL:
screen.listen()
# these methods snake.up ,,, we have in a snake class (up = 90, down = 270, left = 180, right = 0)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    # while the game is on the screen is going to be updated every 0.1 second
    # It is saying delay for 0.1 sec and then update:
    screen.update()
    time.sleep(0.1)
    # every time the screen refreshes we get the snake to move forwards by one step
    snake.move()

    # DETECT COLLISION WITH THE FOOD
    # if the snake head is within 15 px of the food or closer they have collided
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        print("nom nom nom")
        # when the snake collide with the food we increase the score:
        score.increase_score()


    # # DETECT COLLISION WITH THE TAIL METHOD 1:
    # # we can loop through our list of segments in the snake
    # for segment in snake.segments:
    #     # if head has distance from any segment in segments list less than 10 px - that a collision
    #     # if the head collides with any segment in the tail: trigger GAME OVER
    #     # the first segment is the head so we should exclude it from the list of segments
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         score.game_over()

    # DETECT COLLISION WITH THE TAIL METHOD 2 SLICING:
        # we can loop through our list of segments in the snake using slicing method of python
        # we are taking all positions inside the list without the first head segment
        for segment in snake.segments[1:]:
            # if head has distance from any segment in segments list less than 10 px - that a collision
            # if the head collides with any segment in the tail: trigger GAME OVER

            if snake.head.distance(segment) < 10:
                game_is_on = False
                score.game_over()






    # DETECT COLLISION WITH THE WALL
    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False











screen.exitonclick()