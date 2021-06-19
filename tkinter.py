#Importing
from tkinter import *
#Main Screen
a=Tk()
a.geometry("500x500")
a.config(bg="silver")




def clicked():
  print(name.get())



#Wigits
Label(a,text="Name"bg="blue",fg="red").pack()
Button(a,text="Clicked"bg="blue",fg="red",command=clicked).pack()
name=Entry().pack()
