import turtle
import random


class Polygon:

    def __init__(self, num_sides=3, size=1, orientation=0, location_x=0, location_y=0, color=(0, 0, 0), border_size=1,
                 reduction_ratio=0.618):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location_x = location_x
        self.location_y = location_y
        self.color = color
        self.border_size = border_size
        self.reduce = reduction_ratio

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location_x, self.location_y)
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def get_new_color(self):
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    def startup(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

    def turtle_new_location(self):
        turtle.penup()
        turtle.forward(self.size * (1 - self.reduce) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - self.reduce) / 2)
        turtle.right(90)
        self.location_x = turtle.pos()[0]
        self.location_y = turtle.pos()[1]

    def draw(self, sides: int, num_range=(20, 40), t: int = 0):
        self.num_sides = sides
        self.num = random.randint(num_range[0], num_range[1])
        self.startup()
        for _ in range(self.num):
            self.random_polygon()
            self.draw_polygon()
            if t == 1:
                self.turtle_new_location()

    def random_polygon(self):
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location_x = random.randint(-300, 300)
        self.location_y = random.randint(-200, 200)
        self.color = self.get_new_color()
        self.border_size = random.randint(1, 10)

    def input_choice_run(self):
        choice = int(input(f"Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
        if choice == 1:
            self.draw(3)
            turtle.done()
        elif choice == 2:
            self.draw(3)
            turtle.done()
        elif choice == 3:
            self.draw(5)
            turtle.done()
        elif choice == 4:
            self.draw(3, (3, 12))
            self.draw(4, (3, 12))
            self.draw(5, (3, 12))
            turtle.done()
        elif choice == 5:
            self.draw(3, t=1)
            turtle.done()
        elif choice == 6:
            self.draw(4, t=1)
            turtle.done()
        elif choice == 7:
            self.draw(5, t=1)
            turtle.done()
        elif choice == 8:
            self.draw(3, (3, 12), t=1)
            self.draw(4, (3, 12), t=1)
            self.draw(5, (3, 12), t=1)
            turtle.done()
        elif choice == 9:
            self.draw(3, (1, 10))
            self.draw(4, (1, 10))
            self.draw(5, (1, 10))
            self.draw(3, (1, 10), t=1)
            self.draw(4, (1, 10), t=1)
            self.draw(5, (1, 10), t=1)
            turtle.done()


art = Polygon()
art.input_choice_run()
