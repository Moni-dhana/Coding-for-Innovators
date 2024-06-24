import turtle
my_turtle = turtle. Turtle()
def square(length, angle):
    my_turtle. forward(length)
    my_turtle. right(angle)
    my_turtle. forward(length)
    my_turtle. right(angle)
    my_turtle. forward(length)
    my_turtle. right(angle)
    my_turtle. forward(length)
for i in range(40):
    square(100, 90)
    my_turtle .right(100)    