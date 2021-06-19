#Importing
from tkinter import *
#Main Screen
a=Tk()
a.geometry("500x500")
a.config(bg="silver")




def clicked():
  print("Clicked")



#Wigits
Label(a,bg="blue",fg="red").pack()
Button(a,bg="blue",fg="red",command=clicked).pack()
