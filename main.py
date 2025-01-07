import tkinter
from tkinter import *

window = Tk()
window.title("Rechner")
window.geometry("315x350+1500+100")
window.resizable(False, False)
window.configure(bg = "#7F7F7F")

equation = ""

def show(value):
    global equation
    equation += value
    calcscreen.config(text= equation)

def clear():
    global equation
    equation=""
    calcscreen.config(text= equation)

def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result= eval(equation)
        except:
            result="Error"
            equation=""
    calcscreen.config(text= result)

calcscreen = Label(window, width=25, height=2, text="", font=("MS Sans Serif",30))
calcscreen.pack()

Button(window, text="AC", width=5, height=1, font=("MS Sans Serif",15,"bold"), bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=0,y=100)
Button(window, text="/", width=5, height=1, font=("MS Sans Serif",15,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("/")).place(x=80,y=100)
Button(window, text="%", width=5, height=1, font=("MS Sans Serif",15,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("%")).place(x=160,y=100)
Button(window, text="*", width=5, height=1, font=("MS Sans Serif",15,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("*")).place(x=240,y=100)
Button(window, text="7", width=5, height=1, font=("MS Sans Serif",15,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("7")).place(x=0,y=150)
Button(window, text="8", width=5, height=1, font=("MS Sans Serif",15,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("8")).place(x=80,y=150)
Button(window, text="9", width=5, height=1, font=("MS Sans Serif",15,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("9")).place(x=160,y=150)
Button(window, text="-", width=5, height=1, font=("MS Sans Serif",15,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("-")).place(x=240,y=150)
Button(window, text="4", width=5, height=1, font=("MS Sans Serif",15,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("4")).place(x=0,y=200)
Button(window, text="5", width=5, height=1, font=("MS Sans Serif",15,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("5")).place(x=80,y=200)
Button(window, text="6", width=5, height=1, font=("MS Sans Serif",15,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("6")).place(x=160,y=200)
Button(window, text="+", width=5, height=1, font=("MS Sans Serif",15,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("+")).place(x=240,y=200)
Button(window, text="1", width=5, height=1, font=("MS Sans Serif",15,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("1")).place(x=0,y=250)
Button(window, text="2", width=5, height=1, font=("MS Sans Serif",15,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("2")).place(x=80,y=250)
Button(window, text="3", width=5, height=1, font=("MS Sans Serif",15,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("3")).place(x=160,y=250)
Button(window, text="0", width=11, height=1, font=("MS Sans Serif",15,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("0")).place(x=0,y=300)
Button(window, text=".", width=5, height=1, font=("MS Sans Serif",15,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show(".")).place(x=160,y=300)
Button(window, text="=", width=5, height=3, font=("MS Sans Serif",15,"bold"), bd=1,fg="#fff",bg="#ffa500",command=lambda: calculate()).place(x=240,y=250)

window.mainloop()