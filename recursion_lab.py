'''
Using the turtle library, create a fractal pattern.
You may use heading/forward/backward or goto and fill commands to draw
your fractal.  Ideas for your fractal pattern might include
examples from the chapter.  You can find many fractal examples online,
but please make your fractal unique.  Experiment with the variables
to change the appearance and behavior.

Give your fractal a depth of at least 5.  Ensure the fractal is contained on the screen (at whatever size you set it).  Have fun.
(35pts)
'''

import turtle

my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_screen = turtle.Screen()

color_list = ["black", "blue", "purple"]
def draw(my_turtle, my_screen, x, y, heading, dist, depth, color_list):
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.setheading(heading)
    my_turtle.down()
    my_turtle.forward(dist)

    new_dist = dist//1.56
    new_x = my_turtle.xcor()
    new_y = my_turtle.ycor()
    my_turtle.color(color_list[depth%len(color_list)])
    if depth > 0 :
        draw(my_turtle, my_screen, new_x, new_y, heading + 140, new_dist, depth -1, color_list)
        draw(my_turtle, my_screen, new_x, new_y, heading - 140, new_dist, depth -1, color_list)

my_turtle.speed(0)
my_turtle.width(2)

#for i in range(0, 360, 90):
    #draw(my_turtle, my_screen, 0, 0, i, 250, 5, color_list)

#draw(my_turtle, my_screen, 0, 0, 0, 150, 10, color_list)

for i in range(0, 360, 90):
    draw(my_turtle, my_screen, 0, 0, i, 100, 5, color_list)


my_screen.exitonclick()