from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#importing database
from database import DbConnect
#from showdetails import Listtickets
dbconnect=DbConnect()#creating object or instance of imported class

root=Tk()
root.title("TICKET RESERVATION")
root.configure(background="#e1d8b2")#give backgroubd colour to main body
#now for all labels
style=ttk.Style()
style.theme_use("classic")
style.configure("TLabel",background="#e1d8b2")

#now for buttons also same colour
style.configure("TButton",background="#e1d8b2")
#now for radio buttons
style.configure("TRadiobutton",background="#e1d8b2")


#SETTING LABEL AND BOX
ttk.Label(root,text="FULL NAME: ").grid(row=0,column=0,pady=10,padx=5)
entername=ttk.Entry(root,width=30,font=('Arial',16))
entername.grid(row=0,column=1,columnspan=2,pady=10)

#SETTING RADIO BUTTON
spangender=StringVar()
spangender.set('MALE')
ttk.Radiobutton(root,text="MALE",variable=spangender,value="MALE").grid(row=1,column=1)
ttk.Radiobutton(root,text="FEMALE",variable=spangender,value="FEMALE").grid(row=1,column=2)

#SETTING COMMENT BOX
textcomment=Text(root,width=30,height=10,font=("Arial",14))#dont use ttk.Text because text is not a part of tkinter
textcomment.grid(row=3,column=1,columnspan=2)
ttk.Label(root,text="GENDER: ").grid(row=1,column=0)

ttk.Label(root,text="COMMENT: ").grid(row=3,column=0)
b1Button=ttk.Button(root,text="SUBMIT")
b1Button.grid(row=4,column=3)

#b1List=ttk.Button(root,text="List Rev.")
#b1List.grid(row=4,column=2)


#defining function on clicking
def ButtonClick():
    print("FULL NAME:{}".format(entername.get()))
    print("GENDER:{}".format(spangender.get()))
    print("COMMENT:{}".format(textcomment.get(1.0,'end')))
    #adding to database
    #msg variable because after adding we get some message
    msg=dbconnect.Add(entername.get(),spangender.get(),textcomment.get(1.0,'end'))
    #now to show the message
    messagebox.showinfo(title="Add Info",message=msg)
    #after adding 1 message you have to clear the box for that
    entername.delete(0,'end')
    textcomment.delete(1.0,'end')

#def ButtonList():
    #listTickets = Listtickets()


b1Button.config(command=ButtonClick)
#b1List.config(command=ButtonList)

root.mainloop()
