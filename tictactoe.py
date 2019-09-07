from tkinter import *
from tkinter import ttk #for adding style to window means add buttons
from tkinter import messagebox

#defining global variables
p1=[]#list to collect all selected buttons by player1
p2=[]#list to collect all selected buttons by player2
#bfdefault active player is 1
activeplayer=1


root=Tk()#tkinter object means main frame is made by this only if you dont
#write this main empty frame dosent forms

root.title("Tic Tac Toe: Player 1")

#FOR ADDING THEME IN OUR WINDOW
style=ttk.Style()#creating object for style
style.theme_use('classic')

#adding buttons
b1=ttk.Button(root,text=' ')#adding button to frame
b1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)#positioning

#now on clicking that button we want to get some output as a id.
#so for that we define one function that will

b1.config(command=lambda:buttonclick(1))#here we are calling buttonclick fun

#here we have write a lambda fun because if we dont write it then the our called function
#returns null value and command holds null value and give error
#so by writting lambda we can holds the value of our called function

def buttonclick(id):
    #to access our variables
    global activeplayer
    global p1
    global p2

    if (activeplayer==1):
        setlayout(id,"X")
        p1.append(id)
        #after 1 player title get change to 2 player is active
        root.title("Tic Tac Toe: Player 2")
        activeplayer=2
        print("P1 {}".format(p1))
    elif (activeplayer==2):
        setlayout(id,"O")
        p2.append(id)
        #after 2 player title get change to 1 player is active
        root.title("Tic Tac Toe: Player 1")
        activeplayer=1
        print("P2 {}".format(p2))
    #after every action of clicking button we check for winner
    checkwinner()

def setlayout(id,playersymbol):
    if id==1:
        b1.config(text=playersymbol)
        #dont allow other to click on same button
        b1.state(['disabled'])
    elif id==2:
        b2.config(text=playersymbol)
        b2.state(['disabled'])
    elif id==3:
        b3.config(text=playersymbol)
        b3.state(['disabled'])
    elif id==4:
        b4.config(text=playersymbol)
        b4.state(['disabled'])
    elif id==5:
        b5.config(text=playersymbol)
        b5.state(['disabled'])
    elif id==6:
        b6.config(text=playersymbol)
        b6.state(['disabled'])
    elif id==7:
        b7.config(text=playersymbol)
        b7.state(['disabled'])
    elif id==8:
        b8.config(text=playersymbol)
        b8.state(['disabled'])
    elif id==9:
        b9.config(text=playersymbol)
        b9.state(['disabled'])


    #print("ID:{}".format(id))
#this above code is for only one button for 9 buttons we copy same code and just change its
#id and position

#for 2 button
b2=ttk.Button(root,text=' ')
b2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
b2.config(command=lambda:buttonclick(2))

#for 3 button
b3=ttk.Button(root,text=' ')
b3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
b3.config(command=lambda:buttonclick(3))

#for 4 button
b4=ttk.Button(root,text=' ')
b4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
b4.config(command=lambda:buttonclick(4))

#for 5 button
b5=ttk.Button(root,text=' ')
b5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
b5.config(command=lambda:buttonclick(5))

#for 6button
b6=ttk.Button(root,text=' ')
b6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
b6.config(command=lambda:buttonclick(6))

#for 7 button
b7=ttk.Button(root,text=' ')
b7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
b7.config(command=lambda:buttonclick(7))

#for 8 button
b8=ttk.Button(root,text=' ')
b8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
b8.config(command=lambda:buttonclick(8))

#for 9 button
b9=ttk.Button(root,text=' ')
b9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
b9.config(command=lambda:buttonclick(9))


def checkwinner():
    winner=-1#if all the box get fill and no one is able to make line then no one is winner hence -1 case
    if((1 in p1) and (2 in p1) and (3 in p1)):
        winner=1
    if ((1 in p2) and (2 in p2) and (3 in p2)):
        winner =2

    if ((4 in p1) and (5 in p1) and (6 in p1)):
        winner = 1
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        winner = 2

    if ((7 in p1) and (8 in p1) and (9 in p1)):
        winner = 1
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        winner = 2

    if ((1 in p1) and (4 in p1) and (7 in p1)):
        winner = 1
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        winner = 2

    if ((2 in p1) and (5 in p1) and (8 in p1)):
        winner = 1
    if ((2 in p2) and (5 in p2) and (8 in p2)):
        winner = 2
    if ((3 in p1) and (6 in p1) and (9 in p1)):
        winner = 1
    if ((3 in p2) and (6 in p2) and (9 in p2)):
        winner = 2
#for cross line
    if ((1 in p1) and (5 in p1) and (9 in p1)):
        winner = 1
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        winner = 2

    if ((2 in p1) and (5 in p1) and (7 in p1)):
        winner = 1
    if ((2 in p2) and (5 in p2) and (7 in p2)):
        winner = 2


    if winner==1:
        messagebox.showinfo(title="CONGRATES",message="PLAYER 1 IS WINNER")
    elif winner==2:
        messagebox.showinfo(title="CONGRATES",message="PLAYER 2 IS WINNER")
    #else:
       # messagebox.showinfo(title="SORRY!", message="NO ONE IS WINNER")
root.mainloop()#to remain screen open