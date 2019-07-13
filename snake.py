import turtle
import time
import random
#initializing score variable
score=0
highscore=0
#to move food randomly
delay=0.1
#to make delay in moving of head
#set up the screen
wn=turtle.Screen()
wn.title("snake game by mmra")
wn.bgcolor("red")
wn.setup(width=600 ,height=600)
wn.tracer(0) #turns off screen updates
#snake head creation
head=turtle.Turtle() #creating head object
#now some properties of head
head.speed(0) #animation speed of head it is fastest one
head.shape("square")
head.color("black")
head.penup()#not to draw moving path
head.goto(0,0)#initial start position
head.direction="stop"



#now we make our food
#so for that we make one new turtle
#object of food

food = turtle.Turtle()
food.speed(0)#this is not a speed its animation speed
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,100)
#we are making list here (segment) in which we add block continuously after each collision
#adding new segments at the back after collision
segment=[]


#now to show score we create object pen with turtle
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 HighScore:0",align="center",font=("Courier",24,"normal"))


#now we have to move our head on our screen so we make functions
def move():
    #if we want to move head up in y direction
    if head.direction=="up":
        #head moves in y direction every time by 20 px
        y = head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        #head moves in y direction down every time by 20 px
        y = head.ycor()
        head.sety(y-20)

    if head.direction=="right":
        #head moves in x direction every time by 20 px
        x = head.xcor()
        head.setx(x+20)

    if head.direction=="left":
        #head moves in y direction every time by 20 px
        x = head.xcor()
        head.setx(x-20)

#now we make some function so we can command our head
def go_up():
    if head.direction != "down":
        head.direction="up"

def go_down():
    if head.direction != "up":
        head.direction="down"

def go_right():
    if head.direction != "left":
        head.direction="right"

def go_left():
    if head.direction != "right":
        head.direction="left"

#now we have to connects keyboards keys with our fuction so we press a key and action performs
wn.listen()#means it listen keypress
wn.onkeypress(go_up, "Up")#by pressing arrows /no need to use round braces while calling
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")


#main game loop continuously runs every time
while True:
    wn.update()#update the screen

    #check for collision after collision with wall
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)#after collision delay of 1 sec
        head.goto(0,0)#send head to 0,0 position
        head.direction="stop"#and stop head there
        #but after this segment not get disappear
        #so to disappear segment we have to make list empty
        for i in segment:
            i.goto(1000,1000)#this 1000 position can be any value but it should be greater so that it is out of frame

        segment.clear()#this thing only get back our head to intial without other blocks and blocks are at random position
        #reset score after collision with wall
        #shortent our delay
        delay=0.1

        score=0
        pen.clear()

        pen.write("Score:{} HighScore:{}".format(score, highscore), align="center", font=("Courier", 24, "normal"))

    #check for collision with the food
    if head.distance(food)<20:
        #move food randomly
        x=random.randint(-290,290)#290+290=598 and screen is of 600 px
        y = random.randint(-290, 290)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segment.append(new_segment)
        #shortent delay after collision with food
        delay=0.1

        #increase the score after collision
        score +=10
        if score>highscore:
            highscore=score
        pen.clear()

        pen.write("Score:{} HighScore:{}".format(score,highscore),align="center",font=("Courier",24,"normal"))


    #move the end segments first in reverse order
    for index in range(len(segment)-1, 0 , -1):
        #if snake moves in x direction and by below line block 2 moves towards block 1 because 2-1=1 and xcor() means in x direction
        x=segment[index-1].xcor()
        #same if snake moves in y direction
        y=segment[index-1].ycor()
        #combine goto it can be any
        segment[index].goto(x,y) #index = 9 and index-1 =9-1=8 9 goes to 8
    #we have to move our segment 0 which was next to head to the postion of head
    if len(segment)>0:
        #in the above for loop if only 1 seg is there at the 0 position then
        #len_seg=1 and 1-1=0 / and then to start from 0 and end at 0 in for loop doesnt make sense
        #hence we write this condition when if only one seg is present
        x=head.xcor()
        y=head.ycor()
        segment[0].goto(x,y)

    move()
    #check for the head collision with body
    for i in segment:
        if i.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for i in segment:
                i.goto(1000,
                       1000)  # this 1000 position can be any value but it should be greater so that it is out of frame

            segment.clear()  # this thing only get back our head to intial without other blocks and blocks are at random position
            score = 0

            dealy=0.1
            pen.clear()

            pen.write("Score:{} HighScore:{}".format(score, highscore), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)#to produce delay of 0.1 sec



wn.mainloop()
