import turtle


#define the function
#for hexagon
def form_hex(side):
     for i in range(6):
          my_pen.fd(side)
          my_pen.left(300)
          side-=2

#forming the window screen
tut= turtle.Screen()
tut.bgcolor("black")
tut.title("Turtle")


my_pen= turtle.Turtle()
my_pen.color("blue")

tut=turtle.Screen()

#ffor different sizes
side=150
 
for i in range(5):
    form_hex(side)
    side-=12
