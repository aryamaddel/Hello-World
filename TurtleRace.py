import turtle

first = turtle.Turtle()
first.color('red')
first.shape('turtle')
first.speed(1)
second = turtle.Turtle()
second.color('blue')
second.shape('turtle')
second.speed(1)


def get_in_position(turtle):
    turtle.penup()
    if turtle == first:
        turtle.goto(-200, -50)
    else:
        turtle.goto(-200, 50)
    turtle.pendown()


def draw_finish_line(turtle):
    turtle.penup()
    turtle.goto(200, 0)
    turtle.pendown()
    turtle.goto(200, 150)
    turtle.goto(200, -150)


draw_finish_line(first)
get_in_position(first)
get_in_position(second)

while first.xcor() < 200 and second.xcor() < 200:
    if first.xcor() > 200:
        turtle.write('First turtle won!', font=('Arial', 16, 'bold'))
        break
    elif second.xcor() > 200:
        turtle.write('Second turtle won!', font=('Arial', 16, 'bold'))
        break
    dice = int(turtle.numinput(
        title='Dice', prompt='first turtle, roll the dice (1-6)'))
    first.forward(dice*20)
    dice = int(turtle.numinput(
        title='Dice', prompt='second turtle, roll the dice (1-6)'))
    second.forward(dice*20)


turtle.done()
