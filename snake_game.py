import turtle
import os
import time
import random
delay = 0.1 


#Set up the screen

window = turtle.Screen()
window.title("Snake Game by @cagataysen")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0) #turns on/off animation

# Snake head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()  #no drawing when moving
head.goto(0,0)
head.direction = "stop"

# Snake food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()  #no drawing when moving
food.goto(0,100)


#Functions

def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"



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
        
        # head.sety(head.xcor() + 20) tek satırda böyle de yazabiliriz

#Keyboard bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")




#Main game loop

while True:
    window.update() 

    if head.distance(food) < 20:
        #Move the food to a random spot
        x = random.randint(-290,290)
        y = random.randint(-290, 290)
        food.goto(x, y)
    move()

    time.sleep(delay)



os.system("PAUSE")