import turtle
import time
import random

# Constants
DELAY = 0.1
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FOOD_SIZE = 20
MOVE_DISTANCE = 20
FONT = ("Courier", 24, "normal")

class Game:
    def __init__(self):
        self.points = 0
        self.points_to_beat = 0
        self.segments = []
        self.delay = DELAY

        # Screen setup
        self.wn = turtle.Screen()
        self.wn.title("Snake Game by Vivek 😁")
        self.wn.bgcolor("Beige")
        self.wn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.wn.tracer(0)

        # Pen setup
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("circle")
        self.pen.color("black")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.update_score()

        # Snake and food setup
        self.head = self.create_turtle("circle", "red", (0, 0))
        self.head.direction = "stop"
        self.food = self.create_turtle("square", "blue", (0, 100))

        # Keyboard bindings
        self.wn.listen()
        self.wn.onkeypress(self.go_up, "w")
        self.wn.onkeypress(self.go_down, "s")
        self.wn.onkeypress(self.go_left, "a")
        self.wn.onkeypress(self.go_right, "d")

    def create_turtle(self, shape: str, color: str, position: tuple) -> turtle.Turtle:
        t = turtle.Turtle()
        t.speed(0)
        t.shape(shape)
        t.color(color)
        t.penup()
        t.goto(position)
        return t

    def update_score(self):
        self.pen.clear()
        self.pen.write(f"points_punktzahl: {self.points}  Top_score👻: {self.points_to_beat}", align="center", font=FONT)

    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + MOVE_DISTANCE)
        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - MOVE_DISTANCE)
        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - MOVE_DISTANCE)
        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + MOVE_DISTANCE)

    def reset(self):
        time.sleep(1)
        self.head.goto(0, 0)
        self.head.direction = "stop"
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.points = 0
        self.delay = DELAY
        self.update_score()

    def check_collisions(self):
        if abs(self.head.xcor()) > SCREEN_WIDTH // 2 - MOVE_DISTANCE or abs(self.head.ycor()) > SCREEN_HEIGHT // 2 - MOVE_DISTANCE:
            self.reset()

        for segment in self.segments:
            if segment.distance(self.head) < FOOD_SIZE:
                self.reset()

        if self.head.distance(self.food) < FOOD_SIZE:
            x = random.randint(-SCREEN_WIDTH // 2 + MOVE_DISTANCE, SCREEN_WIDTH // 2 - MOVE_DISTANCE)
            y = random.randint(-SCREEN_HEIGHT // 2 + MOVE_DISTANCE, SCREEN_HEIGHT // 2 - MOVE_DISTANCE)
            self.food.goto(x, y)
            new_segment = self.create_turtle("circle", "black", self.head.position())
            self.segments.append(new_segment)
            self.delay -= 0.001
            self.points += 10
            if self.points > self.points_to_beat:
                self.points_to_beat = self.points
            self.update_score()

    def move_segments(self):
        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)
        if self.segments:
            x = self.head.xcor()
            y = self.head.ycor()
            self.segments[0].goto(x, y)

    def run(self):
        while True:
            self.wn.update()
            self.check_collisions()
            self.move_segments()
            self.move()
            time.sleep(self.delay)

if __name__ == "__main__":
    game = Game()
    game.run()
