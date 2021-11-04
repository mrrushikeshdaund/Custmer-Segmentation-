from tkinter import *
from tkinter import messagebox

base = Tk()
base.title("Tik Tko Game")
base.configure(bg="#000000")
base.geometry("700x600")



symbol = "X"

def one():
    b1.configure(text=symbol)
    return 1

def two():
    b2.configure(text=symbol)
    return 2

def three():
    b3.configure(text=symbol)
    return 3


def four():
    b4.configure(text=symbol)
    return 4

def five():
    b5.configure(text=symbol)
    return 5

def six():
    b6.configure(text=symbol)
    return 6

def seven():
    b7.configure(text=symbol)
    return 7

def eight():
    b8.configure(text=symbol)
    return 8

def nine():
    b9.configure(text=symbol)
    return 9


l = Label(base,text="Tik Tko Game",font=("Arial Bold",35),bg="#000000",fg="#FFD700")
l.place(x=230,y=10)


b1 = Button(base,text=" ",width=5,bd=5,height=3,font=("Arial Bold",15),bg="#DCDCDC",command=one)
b1.place(x=200,y=130)

b2 = Button(base,text=" ",width=5,bd=5,height=3,font=("Arial Bold",15),bg="#DCDCDC",command=two)
b2.place(x=300,y=130)

b3 = Button(base,text=" ",width=5,bd=5,height=3,font=("Arial Bold",15),bg="#DCDCDC",command=three)
b3.place(x=400,y=130)

b4 = Button(base,text=" ",width=5,bd=5,height=3,font=("Arial Bold",15),bg="#DCDCDC",command=four)
b4.place(x=200,y=250)

b5 = Button(base,text=" ",width=5,bd=5,height=3,font=("Arial Bold",15),bg="#DCDCDC",command=five)
b5.place(x=300,y=250)

b6 = Button(base,text=" ",width=5,bd=5,height=3,font=("Arial Bold",15),bg="#DCDCDC",command=six)
b6.place(x=400,y=250)

b7 = Button(base,text=" ",width=5,bd=5,height=3,font=("Arial Bold",15),bg="#DCDCDC",command=seven)
b7.place(x=200,y=370)

b8 = Button(base,text=" ",width=5,bd=5,height=3,font=("Arial Bold",15),bg="#DCDCDC",command=eight)
b8.place(x=300,y=370)

b9 = Button(base,text=" ",width=5,bd=5,height=3,font=("Arial Bold",15),bg="#DCDCDC",command=nine)
b9.place(x=400,y=370)

base.mainloop()