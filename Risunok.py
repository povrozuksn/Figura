import turtle 
t = turtle.Turtle()
t.shape()
t.width(1)
t.color('white', 'orange')

t.penup()
t.goto(0, -200)
t.pendown()

t.speed(0)
t.begin_fill()
      
for g in range(12):
    for i in range(90):
        t.forward(100)
        t.left(65)
        
    t.right(57)
                
t.end_fill()    

turtle.done()
