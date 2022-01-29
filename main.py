from turtle import Screen
from snake import Snake
from time import sleep
from food import Food
from score import ScoreBoard

# screen setup
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game 🐍")
my_screen.tracer(0)

# snake object
snake = Snake()

# food object
food = Food()

# Score object
score = ScoreBoard()

# screen listen events
my_screen.listen()
my_screen.onkeypress(fun=snake.up, key="Up")
my_screen.onkeypress(fun=snake.down, key="Down")
my_screen.onkeypress(fun=snake.left, key="Left")
my_screen.onkeypress(fun=snake.right, key="Right")

# game status variable game on or over?
is_game_on = True

# game loop
while is_game_on:
    snake.move()
    my_screen.update()
    sleep(0.1)
    if food.timmy.distance(snake.segment_head.pos()) <= 10:
        food.refresh()
        snake.length_increase()
        score.score_increase()
    if snake.collision_wall() or snake.collision_tail():
        # is_game_on = False
        # score.game_over()
        sleep(1)
        score.refresh_score()
        score.score_board()
        snake.snake_refresh()


# screen holding
my_screen.exitonclick()
