import turtle

myturtle = turtle.Turtle()

myturtle.penup()
myturtle.goto(-300, 75)
myturtle.pendown()

# relative move
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)

myturtle.forward(200)

lowleft = 50, 75
lowright = 100, 75
upright = 100, 200
upleft = 50, 200

# absolute move
myturtle.penup()
myturtle.goto(lowleft)
myturtle.pendown()
myturtle.goto(lowright)
myturtle.goto(upright)
myturtle.goto(upleft)
myturtle.goto(lowleft)



turtle.done()