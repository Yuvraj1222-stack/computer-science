import turtle

atishay=turtle.Turtle()

atishay.forward(100)

atishay.right(90)

atishay.forward(100)

atishay.pencolor("cyan")

atishay.right(90)

atishay.forward(100)

atishay.pencolor("purple")

atishay.right(90)

atishay.forward(100)

atishay.forward(50)

atishay.right(60)

atishay.pencolor("blue")

atishay.forward(50)

atishay.right(60)

atishay.forward(65)

atishay.right(60)

atishay.forward(100)

atishay.pencolor("red")

atishay.penup()

atishay.goto(-180,-180)

atishay.pendown()
atishay.pensize(20)

for i in range(20):
    if i % 2 ==0:
        atishay.pencolor("cyan")
    else:
        atishay.pencolor("pink")
    atishay.circle(10*i)

    
    atishay.goto(-180,-180)
    





    
