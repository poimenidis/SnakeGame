import random
import time
import turtle

if __name__ == "__main__":

    delay = 0.1

    # Set up the screen
    window = turtle.Screen()
    window.title("Snake Game by Kostas Poime")
    window.bgcolor("purple")
    window.setup(width=1000, height=700)
    window.tracer(0)


    # Snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("circle")
    head.color("white")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"

    #Snake food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("square")
    food.color("red")
    food.penup()
    food.goto(0,100)

    # Functions
    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)

        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    def go_up():
        head.direction = "up"

    def go_down():
        head.direction = "down"

    def go_left():
        head.direction = "left"

    def go_right():
        head.direction = "right"


    # Keyboard Bindings
    window.listen()
    window.onkeypress(go_up, 'w')
    window.onkeypress(go_down, 's')
    window.onkeypress(go_left, 'a')
    window.onkeypress(go_right, 'd')


    # Main game loop
    while True:
        window.update()

        if head.distance(food) < 20:
            #Move the food randomly
            x = random.randint(-290,290)
            y = random.randint(-290, 290)
            food.goto(x,y)

        move()
        time.sleep(delay)

    window.mainloop()